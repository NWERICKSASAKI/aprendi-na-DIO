import sqlalchemy as sa
from datetime import datetime, timezone

from src.database import database
from src.models.cliente import cliente, pessoa_fisica, pessoa_juridica
from src.services import conta
from src import exceptions
from src.services import autenticacao


async def _id_existe(id) -> bool:
    query = sa.select(cliente.c.id).where(cliente.c.id == id)
    resultado = await database.fetch_one(query)
    if not resultado:
        return False
    return True

async def _criar_cliente_base(cliente_dict) -> int:
    query = cliente.insert().values(
        endereco = cliente_dict["endereco"],
        cadastrado_em = datetime.now(timezone.utc)
    )
    id = await database.execute(query)
    return id

async def _criar_cliente_pf(id, cliente_dict) -> int:
    query = pessoa_fisica.insert().values(
        cliente_id = id,
        cpf = cliente_dict["cpf"],
        nome = cliente_dict["nome"],
        nascimento = datetime.strptime(str(cliente_dict["nascimento"]), "%Y-%m-%d")
    )
    id = await database.execute(query)
    return id

async def _criar_cliente_pj(id, cliente_dict) -> int:
        query = pessoa_juridica.insert().values(
            cliente_id = id,
            cnpj = cliente_dict["cnpj"],
            razao_social = cliente_dict["razao_social"]
        )
        id = await database.execute(query)
        return id

async def criar_cliente(cliente_dict, dados_usuario_logado) -> int:

    if not dados_usuario_logado:
        raise exceptions.Error_401_UNAUTHORIZED("precisa estar logado!")
    
    if not dados_usuario_logado["is_adm"]:
        raise exceptions.Error_403_FORBIDDEN("Apenas ADM!")

    async with database.transaction(): # commit automático e rollback em caso de erro
        id = await _criar_cliente_base(cliente_dict)
        await autenticacao.criar_senha(id, cliente_dict["senha"])
        match cliente_dict["tipo"]:
            case "pf":
                await _criar_cliente_pf(id, cliente_dict)
            case "pj":
                await _criar_cliente_pj(id, cliente_dict)
        return id


def _mapear_cliente(row) -> dict:
    base = {
        "id": row["id"],
        "contas_id": row["contas_id"],
        "endereco": row["endereco"],
        "cadastrado_em": row["cadastrado_em"].replace(tzinfo=timezone.utc) # para reconverter pro AwareDatetime
    }
    if row["cpf"]:
        return {
            **base,
            "pf_id": row["pf_id"],
            "tipo": "pf",
            "cpf": row["cpf"],
            "nome": row["nome"],
            "nascimento": row["nascimento"]
        }
    if row["cnpj"]:
        return {
            **base,
            "pj_id": row["pj_id"],
            "tipo": "pj",
            "cnpj": row["cnpj"],
            "razao_social": row["razao_social"]
        }
    raise exceptions.Error_404_NOT_FOUND("Cliente sem PF/PJ associado")


async def listar_clientes(dados_usuario_logado) -> list:

    if not dados_usuario_logado["is_adm"]:
        raise exceptions.Error_401_UNAUTHORIZED("Apenas ADM!")

    query = sa.select(
        cliente.c.id,
        cliente.c.endereco,
        cliente.c.cadastrado_em,

        pessoa_fisica.c.id.label("pf_id"),
        pessoa_fisica.c.cpf,
        pessoa_fisica.c.nome,
        pessoa_fisica.c.nascimento,

        pessoa_juridica.c.id.label("pj_id"),
        pessoa_juridica.c.cnpj,
        pessoa_juridica.c.razao_social
    ).select_from(
        cliente
        .outerjoin(pessoa_fisica, pessoa_fisica.c.cliente_id == cliente.c.id)
        .outerjoin(pessoa_juridica, pessoa_juridica.c.cliente_id == cliente.c.id)
    )
    rows = await database.fetch_all(query)
    lista = []
    for row in rows:
        dict_row = dict(row)
        dict_row["contas_id"] = await conta.listar_contas_cliente(dict_row['id'])
        lista.append(_mapear_cliente(dict_row))
    return lista


async def obter_cliente(cliente_id: int, dados_usuario_logado: dict):

    if not dados_usuario_logado["is_adm"] and not cliente_id == dados_usuario_logado["cliente_id"]:
        raise exceptions.Error_403_FORBIDDEN("Você não pode visualizar dados de outros clientes!")

    query = sa.select(
        cliente.c.id.label("id"),
        cliente.c.endereco,
        cliente.c.cadastrado_em,

        pessoa_fisica.c.id.label("pf_id"),
        pessoa_fisica.c.cpf,
        pessoa_fisica.c.nome,
        pessoa_fisica.c.nascimento,

        pessoa_juridica.c.id.label("pj_id"),
        pessoa_juridica.c.cnpj,
        pessoa_juridica.c.razao_social,
    ).select_from(
        cliente
        .outerjoin(pessoa_fisica, pessoa_fisica.c.cliente_id == cliente_id)
        .outerjoin(pessoa_juridica, pessoa_juridica.c.cliente_id == cliente_id)
    ).where(cliente.c.id == cliente_id)
    row = await database.fetch_one(query)
    if not row:
        raise exceptions.Error_404_NOT_FOUND()
    dict_row = dict(row)
    dict_row["contas_id"] = await conta.listar_contas_cliente(cliente_id)
    return _mapear_cliente(dict_row)


async def deletar_cliente(cliente_id: int, dados_usuario_logado: dict) -> bool:

    if not dados_usuario_logado["is_adm"] and not cliente_id == dados_usuario_logado["cliente_id"]:
        raise exceptions.Error_403_FORBIDDEN("Você não pode apagar outro cliente!")
    
    async with database.transaction():
        result = await database.execute(cliente.delete().where(cliente.c.id == cliente_id))
        return result>0 # se apagou alguma linha


async def atualizar_cliente(cliente_id: int, cliente_dict: dict, dados_usuario_logado: dict):

    if not dados_usuario_logado["is_adm"] and not cliente_id == dados_usuario_logado["cliente_id"]:
        raise exceptions.Error_403_FORBIDDEN("Você não pode atualizar dados de outros clientes!")

    if not await _id_existe(cliente_id):
        raise exceptions.Error_404_NOT_FOUND(f"Cliente com ID {cliente_id} não existe")
    
    async with database.transaction():
        tipo = cliente_dict.pop("tipo")

        dados_base = {}
        for k,v in cliente_dict.items():
            if k in cliente.c:
                dados_base[k]=v
        if dados_base:
            await database.execute(cliente.update().values(**dados_base).where(cliente.c.id == cliente_id))

        match tipo:
            case 'pf':
                dados_pf = {}
                for k,v in cliente_dict.items():
                    if k in pessoa_fisica.c:
                        dados_pf[k]=v
                if dados_pf:
                    await database.execute(pessoa_fisica.update().values(**dados_pf).where(pessoa_fisica.c.id == cliente_id))

            case 'pj':
                dados_pj = {}
                for k,v in cliente_dict.items():
                    if k in pessoa_juridica.c:
                        dados_pj[k]=v
                if dados_pj:
                    await database.execute(pessoa_juridica.update().values(**dados_pj).where(pessoa_juridica.c.id == cliente_id))
        
        if "senha" in dados_base:
            await autenticacao.alterar_senha(cliente_dict, dados_usuario_logado)
            
        return
