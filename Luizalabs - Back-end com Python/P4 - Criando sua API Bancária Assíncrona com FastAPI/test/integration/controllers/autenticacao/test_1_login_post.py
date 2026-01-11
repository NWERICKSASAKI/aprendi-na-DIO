from fastapi import status
from httpx import AsyncClient

PREFIXO = "/login/"

async def test_post_login_adm_success(client: AsyncClient):

    # Given
    json_autenticacao = {
        "cliente_id": 99,
        "senha": "tanto-faz",
        "is_adm": True
    }    

    # When
    response = await client.post(PREFIXO, json=json_autenticacao)
    
    # Then
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["access_token"] is not None


async def test_post_login_cliente_success(client: AsyncClient): 

    # Given
    json_autenticacao = {
        "cliente_id": 1,
        "senha": "1234"
    }    

    # When
    response = await client.post(PREFIXO, json=json_autenticacao)
    
    # Then
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["access_token"] is not None


async def test_post_login_cliente_senha_errada(client: AsyncClient):

    # Given
    json_autenticacao = {
        "cliente_id": 1,
        "senha": "senha-errada"
    }    

    # When
    response = await client.post(PREFIXO, json=json_autenticacao)
    
    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_post_login_cliente_usuario_inexistente(client: AsyncClient):
    
    # Given
    json_autenticacao = {
        "cliente_id": 999,
        "senha": "tanto-faz"
    }    

    # When
    response = await client.post(PREFIXO, json=json_autenticacao)
    
    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

