import sqlalchemy as sa
from src.database import database
from src.models.cliente import cliente, pessoa_fisica, pessoa_juridica
from datetime import datetime, timezone

async def _criar_cliente_base(cliente_json) -> int:
    query = cliente.insert().values(
        endereco = cliente_json.endereco,
        cadastrado_em = datetime.now(timezone.utc)
    )
    id = await database.execute(query)
    return id

async def _criar_cliente_pf(id, cliente_json) -> int:
    query = pessoa_fisica.insert().values(
        cliente_id = id,
        cpf = cliente_json.cpf,
        nome = cliente_json.nome,
        nascimento = cliente_json.nascimento
    )
    id = await database.execute(query)
    return id

async def _criar_cliente_pj(id, cliente_json) -> int:
        query = pessoa_juridica.insert().values(
            cliente_id = id,
            cnpj = cliente_json.cnpj,
            razao_social = cliente_json.razao_social
        )
        id = await database.execute(query)
        return id

async def criar_cliente(cliente_json):
    async with database.transaction(): # commit automático e rollback em caso de erro
        id = await _criar_cliente_base(cliente_json)
        match cliente_json.tipo:
            case "pf":
                await _criar_cliente_pf(id, cliente_json)
            case "pj":
                await _criar_cliente_pj(id, cliente_json)
        return id

async def listar_clientes():
    query = cliente.select()
    return await database.fetch_all(query)

def _mapear_cliente(row) -> dict:
    base = {
        "id": row["id"],
        "endereco": row["endereco"],
        "cadastrado_em": row["cadastrado_em"]
    }
    if row["cpf"]:
        return {
            **base,
            "pf_id": row["pf_id"],
            "cpf": row["cpf"],
            "nome": row["nome"],
            "nascimento": row["nascimento"]
        }
    if row["cnpj"]:
        return {
            **base,
            "pj_id": row["pj_id"],
            "cnpj": row["cnpj"],
            "razao_social": row["razao_social"]
        }
    raise ValueError("Cliente sem PF/PJ associado")

async def obter_cliente(cliente_id):
    # query = cliente.select().where(cliente.c.id == cliente_id)

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
        return None
    return _mapear_cliente(row)


async def deletar_cliente(cliente_id: int):
    async with  database.transaction():
        await database.execute(pessoa_fisica.delete().where(pessoa_fisica.c.cliente_id == cliente_id))
        await database.execute(pessoa_juridica.delete().where(pessoa_juridica.c.cliente_id == cliente_id))
        result = await database.execute(cliente.delete().where(cliente.c.id == cliente_id))
        return result>0 # se apagou alguma linha
