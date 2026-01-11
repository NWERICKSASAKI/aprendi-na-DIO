from fastapi import status
from httpx import AsyncClient
from src.services import cliente

PREFIXO = "/clientes/"

async def test_post_sem_autenticacao_failed(client: AsyncClient):

    # Given
    data = {
        "endereco": "Rua 1",
        "senha": "1",
        "tipo": "pf",
        "cpf": "111.111.111-11",
        "nome": "Cliente Dois",
        "nascimento": "1999-01-01"
    }

    # When
    response = await client.post(PREFIXO, json=data)

    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_post_autenticado_adm_success(client: AsyncClient, access_token_adm: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_adm}"}
    data = {
        "endereco": "Rua 2",
        "senha": "2",
        "tipo": "pf",
        "cpf": "222.222.222-22",
        "nome": "Cliente Dois",
        "nascimento": "1999-02-02"
    }

    # When
    response = await client.post(PREFIXO, headers=headers, json=data)

    # Then
    assert response.status_code == status.HTTP_201_CREATED


async def test_post_autenticado_cliente_failed(client: AsyncClient, access_token_cliente_1: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_cliente_1}"}
    data = {
        "endereco": "Rua 3",
        "senha": "3",
        "tipo": "pf",
        "cpf": "333.333.333-33",
        "nome": "Cliente Tres",
        "nascimento": "1999-03-03"
    }
    # When
    response = await client.post(PREFIXO, headers=headers, json=data)

    # Then
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_post_autenticado_adm_sem_json_failed(client: AsyncClient, access_token_adm: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_adm}"}

    # When
    response = await client.post(PREFIXO, headers=headers)

    # Then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
