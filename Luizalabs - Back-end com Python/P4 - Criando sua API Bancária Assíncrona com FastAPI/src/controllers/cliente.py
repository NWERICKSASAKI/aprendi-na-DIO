from fastapi import APIRouter, Depends, status

from src.schemas.cliente import cliente_in, cliente_in_edit
from src.views.cliente import cliente_out
from src.services import cliente as services
from src.services.autenticacao import login_required

from typing import Annotated

router = APIRouter(prefix="/clientes", tags=["Clientes"])

# GET
@router.get("/", response_model=list[cliente_out])
async def listar_clientes(dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    return await services.listar_clientes(dados_usuario_logado)

@router.get("/{cliente_id}", response_model=cliente_out)
async def obter_cliente(cliente_id: int, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    cliente:dict = await services.obter_cliente(cliente_id, dados_usuario_logado)
    return cliente

# POST
@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente_json: cliente_in, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    cliente_id = await services.criar_cliente(cliente_json.model_dump(exclude_unset=True), dados_usuario_logado)
    return f"Cliente id {cliente_id} criado com sucesso!"

# PATCH
@router.patch("/{cliente_id}", status_code=status.HTTP_202_ACCEPTED)
async def atualizar_cliente(cliente_id: int, cliente_json: cliente_in_edit, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    await services.atualizar_cliente(cliente_id, cliente_json.model_dump(exclude_unset=True), dados_usuario_logado)
    return f"Cliente id {cliente_id} editado com sucesso!"

# DELETE
@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(cliente_id: int, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    await services.deletar_cliente(cliente_id, dados_usuario_logado)
    return
