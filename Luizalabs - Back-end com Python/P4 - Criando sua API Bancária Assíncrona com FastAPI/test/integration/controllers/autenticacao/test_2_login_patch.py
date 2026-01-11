from fastapi import status
from httpx import AsyncClient
from src.services.autenticacao import get_senha_do_usuario

PREFIXO = "/login/"

async def test_patch_senha_sem_estar_logado_failed(client: AsyncClient):

    # Given
    json_autenticacao = {
        "cliente_id": 1,
        "senha": "nova-senha"
    }    

    # When
    response = await client.patch(PREFIXO, json=json_autenticacao)
    
    # Then
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_patch_senha_logado_success(client: AsyncClient, access_token_cliente_1: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_cliente_1}"}
    data = {
        "cliente_id": 1,
        "senha": "nova-senha"
    }    

    # When
    response = await client.patch(PREFIXO, json=data, headers=headers)
    senha_no_bd = await get_senha_do_usuario(data["cliente_id"])
    
    # Then

    
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert senha_no_bd == data["senha"]


async def test_patch_senha_outro_usuario_failed(client: AsyncClient, access_token_cliente_1: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_cliente_1}"}
    data = {
        "cliente_id": 2,
        "senha": "nova_senha_do_user_1"
    }    

    # When
    response = await client.patch(PREFIXO, json=data, headers=headers)
    senha_no_bd = await get_senha_do_usuario(data["cliente_id"])
    
    # Then
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert senha_no_bd != data["senha"]


async def test_patch_senha_via_adm_success(client: AsyncClient, access_token_adm: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_adm}"}
    data = {
        "cliente_id": 1,
        "senha": "senha-temporaria"
    }    

    # When
    response = await client.patch(PREFIXO, json=data, headers=headers)
    senha_no_bd = await get_senha_do_usuario(data["cliente_id"])

    # Then
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert senha_no_bd == data["senha"]


async def test_patch_senha_via_adm_cliente_inexistente_failed(client: AsyncClient, access_token_adm: str):

    # Given
    headers = {"Authorization": f"Bearer {access_token_adm}"}
    data = {
        "cliente_id": 999,
        "senha": "senha-temporaria"
    }    

    # When
    response = await client.patch(PREFIXO, json=data, headers=headers)

    # Then
    assert response.status_code == status.HTTP_404_NOT_FOUND


# async def test_patch_senha_via_adm_cliente_inexistente(client: AsyncClient):

#     # override auth
#     app.dependency_overrides[autenticacao.login_required] = lambda: {
#         "cliente_id": 0,
#         "is_adm": True
#     }

#     # Given
#     data = {
#         "cliente_id": 999,
#         "senha": "senha-temporaria"
#     }    

#     # When
#     response = await client.patch(PREFIXO, json=data)

#     # Then
#     assert response.status_code == status.HTTP_404_NOT_FOUND
