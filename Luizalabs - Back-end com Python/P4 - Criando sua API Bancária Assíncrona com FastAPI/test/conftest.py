import asyncio

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from src.config import settings
from src.services.autenticacao import _gerar_token

settings.database_url = "sqlite:///tests.db"

@pytest_asyncio.fixture
async def db(request):

    from src.database import database, engine, metadata

    from src.models.autenticacao import autenticacao
    from src.models.cliente import cliente, pessoa_fisica, pessoa_juridica
    from src.models.conta import conta, conta_corrente, conta_empresarial
    from src.models.transacao import transacao

    await database.connect()
    metadata.create_all(engine)

    def teardown():
        async def _teardown():
            await database.disconnect()
            metadata.drop_all(engine) 
        asyncio.run(_teardown())
    request.addfinalizer(teardown)


@pytest_asyncio.fixture
async def client(db):
    from src.main import app

    transport = ASGITransport(app=app)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    async with AsyncClient(base_url = "http://test", transport=transport, headers=headers) as client:
        yield client


@pytest_asyncio.fixture
async def access_token_cliente_1(client: AsyncClient):
    dados = {
        "cliente_id": 1,
        "is_adm": False
    }
    
    token = _gerar_token(dados["cliente_id"], dados["is_adm"])
    return token["access_token"]


@pytest_asyncio.fixture
async def access_token_cliente_2(client: AsyncClient):
    dados = {
        "cliente_id": 2,
        "is_adm": False
    }
    
    token = _gerar_token(dados["cliente_id"], dados["is_adm"])
    return token["access_token"]


@pytest_asyncio.fixture
async def access_token_adm(client: AsyncClient):
    dados = {
        "cliente_id": 0,
        "is_adm": True
    }
    
    token = _gerar_token(dados["cliente_id"], dados["is_adm"])
    return token["access_token"]


@pytest_asyncio.fixture(autouse=True)
async def criar_cliente_1(db):
    from src.services import cliente
    
    cliente_dict = {
        "endereco": "R. Tanto Faz, sem numero",
        "senha": "1234",
        "tipo": "pf",
        "cpf": "12345678901",
        "nome": "Testonildo da Silva",
        "nascimento": "1993-02-01"
    }

    await cliente.criar_cliente(cliente_dict, {"is_adm": True})


@pytest_asyncio.fixture(autouse=True)
async def criar_cliente_2(db):
    from src.services import cliente
    
    cliente_dict = {
        "endereco": "Rua Empresarial, 1.000",
        "senha": "Senha-Secreta",
        "tipo": "pj",
        "cnpj": "123.456.789/000-1",
        "razao_social": "Testes & CIA"
    }

    await cliente.criar_cliente(cliente_dict, {"is_adm": True})

