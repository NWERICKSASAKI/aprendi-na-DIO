import sqlalchemy as sa
from src.database import database
from src.models.conta import conta, conta_corrente, conta_empresarial
from src.services import transacao as transacao_services
from datetime import datetime, timezone
from src import exceptions

async def _id_existe(id) -> bool:
    query = sa.select(conta.c.id).where(conta.c.id == id)
    resultado = await database.fetch_one(query)
    if not resultado:
        return False
    return True

async def _criar_conta_base(conta_json) -> int:
    query = conta.insert().values(
        saldo = 0,
        cliente_id = conta_json.cliente_id,
        agencia = conta_json.agencia,
        cadastrado_em = datetime.now(timezone.utc)
    )
    id = await database.execute(query)
    return id

async def _criar_conta_corrente(conta_id, conta_json) -> int:
    query = conta_corrente.insert().values(
        conta_id = conta_id,
        limite = conta_json.limite,
        limite_saque = conta_json.limite_saque
    )
    id = await database.execute(query)
    return id

async def _criar_conta_empresarial(conta_id, conta_json) -> int:
    query = conta_empresarial.insert().values(
        conta_id = conta_id,
        emprestimo = 0,
        emprestimo_limite = conta_json.emprestimo_limite
    )
    id = await database.execute(query)
    return id

async def criar_conta(conta_json, dados_usuario_logado: dict) -> int:

    if not dados_usuario_logado:
        raise exceptions.Error_401_UNAUTHORIZED("Precisa estar logado")
    
    if not dados_usuario_logado["is_adm"]:
        raise exceptions.Error_403_FORBIDDEN("apenas ADM!")

    async with database.transaction():
        id = await _criar_conta_base(conta_json)
        match conta_json.tipo:
            case "cc":
                await _criar_conta_corrente(id, conta_json)
            case "ce":
                await _criar_conta_empresarial(id, conta_json)
        return id


def _mapear_conta(row) -> dict:
    base = {
        "id": row["id"],
        "cliente_id": row["cliente_id"],
        "saldo": row["saldo"],
        "agencia": row["agencia"],
        "cadastrado_em": row["cadastrado_em"].replace(tzinfo=timezone.utc)
    }
    if row["cc_id"]:
        return {
            **base,
            "cc_id": row["cc_id"],
            "tipo": "cc",
            "valor_saques": row["valor_saques"],
            "limite": row["limite"],
            "qtd_saques": row["qtd_saques"],
            "limite_saque": row["limite_saque"]
        }
    if row["ce_id"]:
        return{
            **base,
            "ce_id": row["ce_id"],
            "tipo": "ce",
            "emprestimo": row["emprestimo"],
            "emprestimo_limite": row["emprestimo_limite"]
        }
    raise exceptions.Error_404_NOT_FOUND(f"Conta sem CC/CE associado: {dict(row)}")


async def listar_contas(dados_usuario_logado) -> list:

    if not dados_usuario_logado:
        raise exceptions.Error_401_UNAUTHORIZED("precisa estar logado!")

    if not dados_usuario_logado["is_adm"]:
        raise exceptions.Error_403_FORBIDDEN("apenas ADM!")

    query = sa.select(
        conta.c.id,
        conta.c.cliente_id,
        conta.c.saldo,
        conta.c.agencia,
        conta.c.cadastrado_em,

        conta_corrente.c.id.label('cc_id'),
        conta_corrente.c.limite,
        conta_corrente.c.limite_saque,

        conta_empresarial.c.id.label('ce_id'),
        conta_empresarial.c.emprestimo,
        conta_empresarial.c.emprestimo_limite
    ).select_from(
        conta
        .outerjoin(conta_corrente, conta_corrente.c.conta_id == conta.c.id)
        .outerjoin(conta_empresarial, conta_empresarial.c.conta_id == conta.c.id)
    )
    lista = []
    rows = await database.fetch_all(query)
    for row in rows:
        row_dict = dict(row)
        if row_dict["cc_id"]:
            row_dict["qtd_saques"], row_dict["valor_saques"] = await transacao_services.qtd_valor_saques(row_dict["id"])
        row_dict = _mapear_conta(row_dict)
        lista.append(row_dict)
    return lista


async def _retorna_cliente_id_da_conta(conta_id) -> int:
    query = conta.select(conta.c.cliente_id).where(conta.c.id == conta_id)
    result = await database.fetch_one(query)
    return result["cliente_id"]

async def obter_conta(conta_id: int, dados_usuario_logado: dict) -> dict:
    
    cliente_id = await _retorna_cliente_id_da_conta(conta_id)

    if not dados_usuario_logado["is_adm"] and not cliente_id == dados_usuario_logado["cliente_id"]:
        raise exceptions.Error_403_FORBIDDEN("Você não pode visualizar os dados de contas de outros clientes")
    
    if not await _id_existe(conta_id):
        raise exceptions.Error_404_NOT_FOUND(f"Conta com ID {conta_id} não encontrada!")
    
    query = sa.select(
        conta.c.id,
        conta.c.cliente_id,
        conta.c.saldo,
        conta.c.agencia,
        conta.c.cadastrado_em,

        conta_corrente.c.id.label('cc_id'),
        conta_corrente.c.limite,
        conta_corrente.c.limite_saque,

        conta_empresarial.c.id.label('ce_id'),
        conta_empresarial.c.emprestimo,
        conta_empresarial.c.emprestimo_limite
    ).select_from(
        conta
        .outerjoin(conta_corrente, conta_corrente.c.conta_id == conta_id)
        .outerjoin(conta_empresarial, conta_empresarial.c.conta_id == conta_id)
    ).where(conta.c.id == conta_id)
    row = await database.fetch_one(query)
    row_dict = dict(row)
    if row_dict["cc_id"]:
        row_dict["qtd_saques"], row_dict["valor_saques"] = await transacao_services.qtd_valor_saques(conta_id)
    return _mapear_conta(row_dict)


async def exibir_saldo(conta_id: int, dados_usuario_logado: dict) -> float:

    cliente_id = await _retorna_cliente_id_da_conta(conta_id)

    if not dados_usuario_logado["is_adm"] and not cliente_id == dados_usuario_logado["cliente_id"]:
        raise exceptions.Error_403_FORBIDDEN("Você não pode visualizar os dados de contas de outros clientes")

    query = sa.select(
        conta.c.saldo
    ).where(conta.c.id == conta_id)
    row = await database.fetch_one(query)
    if not row:
        raise exceptions.Error_404_NOT_FOUND(f"Conta com ID {conta_id} não encontrada!")
    return row["saldo"]


async def deletar_conta(conta_id: int, dados_usuario_logado: dict) -> bool:

    cliente_id = await _retorna_cliente_id_da_conta(conta_id)
    if not dados_usuario_logado["is_adm"] and not cliente_id == dados_usuario_logado["cliente_id"]:
        raise exceptions.Error_403_FORBIDDEN("Você não pode visualizar os dados de contas de outros clientes")

    async with database.transaction():
        result = await database.execute(conta.delete().where(conta.c.id == conta_id))
        return result>0


async def editar_conta(conta_id: int, conta_json, dados_usuario_logado: dict):

    cliente_id = await _retorna_cliente_id_da_conta(conta_id)
    
    if not dados_usuario_logado["is_adm"] and not cliente_id == dados_usuario_logado["cliente_id"]:
        raise exceptions.Error_403_FORBIDDEN("Você não pode visualizar os dados de contas de outros clientes")


    if not await _id_existe(conta_id):
        raise exceptions.Error_404_NOT_FOUND(f"Conta com ID {conta_id} não encontrada!")
    async with database.transaction():
        dicio_dados = conta_json.model_dump(exclude_unset=True)
        tipo = dicio_dados.pop("tipo")

        dados_base = {}
        for k,v in dicio_dados.items():
            if k in conta.c:
                dados_base[k]=v
        if dados_base:
            await database.execute(conta.update().values(**dados_base).where(conta.c.id == conta_id))
    
        match tipo:
            case "cc":
                dados_cc = {}
                for k,v in dicio_dados.items():
                    if k in conta_corrente.c:
                        dados_cc[k]=v
                if dados_base:
                    await database.execute(conta_corrente.update().values(**dados_cc).where(conta_corrente.c.id == conta_id))

            case "ce":
                dados_ce = {}
                for k,v in dicio_dados.items():
                    if k in conta_empresarial.c:
                        dados_ce[k]=v
                if dados_base:
                    await database.execute(conta_empresarial.update().values(**dados_ce).where(conta_empresarial.c.id == conta_id))
        return


async def listar_contas_cliente(cliente_id) -> list[int]:
    query = sa.select(conta.c.id).where(conta.c.cliente_id == cliente_id)
    rows = await database.fetch_all(query)
    return [row['id'] for row in rows]
