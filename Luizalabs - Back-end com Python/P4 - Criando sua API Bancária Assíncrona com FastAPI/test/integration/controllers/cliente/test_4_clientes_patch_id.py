from fastapi import status
from httpx import AsyncClient
from src.services import cliente

PREFIXO = "/clientes/1"

async def test_patch_1_sem_autenticacao_failed(client: AsyncClient):

    # Given
    data = {
        "endereco": "Rua Editado, 0",
        "tipo": "pf",
        "cpf":"123.456.789-0"
    }

    # When
    response = await client.patch(PREFIXO, json=data)
    endereco = await cliente.obter_cliente(1, {'is_adm':True})

    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert endereco["endereco"] != "Rua Editado, 0"


async def test_patch_1_autenticado_cliente1_success(client: AsyncClient, access_token_cliente_1: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_cliente_1}"}
    data = {
        "endereco": "Rua Editado, 1",
        "tipo": "pf",
        "cpf":"123.456.789-0"
    }

    # When
    response = await client.patch(PREFIXO, headers=headers, json=data)
    endereco = await cliente.obter_cliente(1, {'is_adm':True})
    
    # Then
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert endereco["endereco"] == "Rua Editado, 1"


async def test_patch_1_autenticado_cliente1_sem_json_failed_como_adm(client: AsyncClient, access_token_adm: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_adm}"}

    # When
    response = await client.patch(PREFIXO, headers=headers)
    
    # Then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


async def test_patch_1_autenticado_cliente1_sem_json_failed_como_cliente(client: AsyncClient, access_token_cliente_1: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_cliente_1}"}

    # When
    response = await client.patch(PREFIXO, headers=headers)
    
    # Then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


async def test_patch_1_autenticado_cliente2_failed(client: AsyncClient, access_token_cliente_2: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_cliente_2}"}
    data = {
        "endereco": "Rua Editado, 2",
        "tipo": "pf",
        "cpf":"123.456.789-0"
    }

    # When
    response = await client.patch(PREFIXO, headers=headers, json=data)
    endereco = await cliente.obter_cliente(1, {'is_adm':True})
    
    # Then
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert endereco["endereco"] != "Rua Editado, 2"


async def test_patch_1_autenticado_adm_sucesso(client: AsyncClient, access_token_adm: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_adm}"}
    data = {
        "endereco": "Rua Editado, 3",
        "tipo": "pf",
        "cpf":"123.456.789-0"
    }

    # When
    response = await client.patch(PREFIXO, headers=headers, json=data)
    endereco = await cliente.obter_cliente(1, {'is_adm':True})
    # Then
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert endereco["endereco"] == "Rua Editado, 3"
