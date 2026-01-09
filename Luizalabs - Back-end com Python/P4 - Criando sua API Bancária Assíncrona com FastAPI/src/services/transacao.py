import sqlalchemy as sa
from src.database import database
from src.models.conta import conta, conta_corrente, conta_empresarial
from src.models.transacao import transacao
from src.services import conta as conta_services
from datetime import datetime, timezone, time, date
from src import exceptions

def _mapear_transacao(row):
    return {
        "id": row["id"],
        "conta_id": row["conta_id"],
        "valor": row["valor"],
        "tipo": row["tipo"],
        "com_sucesso": row["com_sucesso"],
        "cadastrado_em": row["cadastrado_em"].replace(tzinfo=timezone.utc)
    }

async def listar_transacoes() -> list:
    rows = await database.fetch_all(transacao.select())
    return [_mapear_transacao(row) for row in rows]


async def visualizar_transacao(transacao_id: int) -> dict:
    row = await database.fetch_one(transacao.select().where(transacao.c.id == transacao_id))
    if not row:
        raise exceptions.Error_404_NOT_FOUND()
    return _mapear_transacao(row)


async def visualizar_extrato_cliente(cliente_id: int) -> list:
    rows = await database.fetch_all(transacao.select().where(transacao.c.conta_id == cliente_id))
    return [_mapear_transacao(row) for row in rows]


async def _cadastrar_transacao(transacao_json, tipo_transacao:str, sucesso:bool) -> int:
    query = transacao.insert().values(
        conta_id = transacao_json.conta_id,
        valor = transacao_json.valor,
        tipo = tipo_transacao,
        com_sucesso = sucesso,
        cadastrado_em = datetime.now(timezone.utc)
    )
    transacao_id: int = await database.execute(query)
    return transacao_id


async def qtd_valor_saques(conta_id) -> tuple[int, float]:
    hoje = date.today()
    inicio = datetime.combine(hoje, time.min)
    fim = datetime.combine(hoje, time.max)

    query_qtd = sa.select(sa.func.count()).select_from(transacao).where(
        transacao.c.conta_id == conta_id,
        transacao.c.tipo == "s",
        transacao.c.cadastrado_em.between(inicio,fim)
    )
    qtd_saques_hoje:int = await database.fetch_val(query_qtd)

    query_valor = sa.select(sa.func.coalesce(sa.func.sum(transacao.c.valor), 0)).where(
        transacao.c.conta_id == conta_id,
        transacao.c.tipo == "s",
        transacao.c.cadastrado_em.between(inicio,fim)
    )
    valor_saques_hoje:float = await database.fetch_val(query_valor)

    return (qtd_saques_hoje, valor_saques_hoje)


async def _transacao_autorizada(transacao_json, tipo_transacao:str, conta_json) -> tuple[bool,str]:
    if tipo_transacao == "s":
        tipo_conta:str = conta_json["tipo"]
        if transacao_json.valor <= conta_json["saldo"]:
            if tipo_conta == 'cc':
                conta_id = conta_json["id"]
                qtd_saques_hoje, valor_saques_hoje = await qtd_valor_saques(conta_id)
                if qtd_saques_hoje >= conta_json["limite"]:
                    return False, "Quantidade de Saques excedidos"
                if valor_saques_hoje + transacao_json.valor>= conta_json["limite_saque"]:
                    return False, "Valor excede limite"
            return True, ""
        return False, "Saldo insuficiente"
    return True, ""


async def _alterar_saldo(transacao_json, tipo:str, conta_json):
    conta_id: int =  transacao_json.conta_id
    mod:int = 1 if tipo=='d' else -1
    saldo_final:float = conta_json["saldo"] + mod * transacao_json.valor
    query = conta.update().values(saldo = saldo_final).where(conta.c.id == conta_id)
    await database.execute(query)
    return


async def realizar_transacao(transacao_json, tipo_transacao:str):
    async with database.transaction():
        conta_id: int = transacao_json.conta_id
        if not await conta_services._id_existe(conta_id):
            raise exceptions.Error_404_NOT_FOUND(f"Conta de ID {conta_id} não encontrada!")
        
        conta_json: dict = await conta_services.obter_conta(conta_id)
        sucesso: bool = True
        if tipo_transacao == 's': # saque
            sucesso, motivo_erro = await _transacao_autorizada(transacao_json, tipo_transacao, conta_json)
        transacao_id: int = await _cadastrar_transacao(transacao_json, tipo_transacao=tipo_transacao, sucesso=sucesso)
        if not sucesso:
            raise exceptions.Error_403_FORBIDDEN(motivo_erro)

        await _alterar_saldo(transacao_json, tipo=tipo_transacao, conta_json=conta_json)
        return transacao_id


async def deletar_transacao_conta(conta_id):
    result = await database.execute(transacao.delete().where(transacao.c.conta_id == conta_id))
    return result>0
