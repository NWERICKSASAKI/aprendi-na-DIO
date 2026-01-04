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
        tipo = cliente_json.tipo,
        cpf = cliente_json.cpf,
        nome = cliente_json.nome,
        nascimento = cliente_json.nascimento
    )
    id = await database.execute(query)
    return id

async def _criar_cliente_pj(id, cliente_json) -> int:
        query = pessoa_juridica.insert().values(
            cliente_id = id,
            tipo = cliente_json.tipo,
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

async def resgatar_cliente(cliente_id):
    query = cliente.select().where(cliente.c.id == cliente_id)
    return await database.fetch_one(query)
