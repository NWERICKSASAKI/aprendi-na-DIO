import sqlalchemy as sa
from src.database import engine
from src.models.cliente import cliente, pessoa_fisica, pessoa_juridica
from datetime import datetime, timezone

def _criar_cliente_base(cliente_json, conn) -> int:
    stmt = cliente.insert().values(
        endereco = cliente_json.endereco,
        cadastrado_em = datetime.now(timezone.utc)
    )
    result = conn.execute(stmt)
    id = result.inserted_primary_key[0]
    return id

def _criar_cliente_pf(id, cliente_json, conn) -> int:
    stmt = pessoa_fisica.insert().values(
        cliente_id = id,
        tipo = cliente_json.tipo,
        cpf = cliente_json.cpf,
        nome = cliente_json.nome,
        nascimento = cliente_json.nascimento
    )
    result = conn.execute(stmt)
    id = result.inserted_primary_key[0]
    return id

def _criar_cliente_pj(id, cliente_json, conn) -> int:
        stmt = pessoa_juridica.insert().values(
            cliente_id = id,
            tipo = cliente_json.tipo,
            cnpj = cliente_json.cnpj,
            razao_social = cliente_json.razao_social
        )
        result = conn.execute(stmt)
        id = result.inserted_primary_key[0]
        return id

def criar_cliente(cliente_json):
    with engine.connect() as conn:
        id = _criar_cliente_base(cliente_json, conn)
        match cliente_json.tipo:
            case "pf":
                _criar_cliente_pf(id, cliente_json, conn)
            case "pj":
                _criar_cliente_pj(id, cliente_json, conn)
        try:
            conn.commit()
        except:
            conn.rollback()


