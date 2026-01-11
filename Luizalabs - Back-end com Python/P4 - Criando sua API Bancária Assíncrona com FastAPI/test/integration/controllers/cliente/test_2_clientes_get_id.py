from fastapi import status
from httpx import AsyncClient

PREFIXO = "/clientes/1"

async def test_get_1_sem_autenticacao_failed(client: AsyncClient):

    # Given

    # When
    response = await client.get(PREFIXO)
    
    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_get_1_autenticado_cliente1_success(client: AsyncClient, access_token_cliente_1: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_cliente_1}"}

    # When
    response = await client.get(PREFIXO, headers=headers)
    
    # Then
    assert response.status_code == status.HTTP_200_OK


async def test_get_1_autenticado_cliente2_failed(client: AsyncClient, access_token_cliente_2: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_cliente_2}"}

    # When
    response = await client.get(PREFIXO, headers=headers)
    
    # Then
    assert response.status_code == status.HTTP_403_FORBIDDEN


async def test_get_1_autenticado_adm_sucesso(client: AsyncClient, access_token_adm: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_adm}"}

    # When
    response = await client.get(PREFIXO, headers=headers)
    
    # Then
    assert response.status_code == status.HTTP_200_OK

