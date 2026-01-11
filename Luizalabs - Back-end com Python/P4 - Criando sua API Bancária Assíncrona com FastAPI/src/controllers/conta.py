from fastapi import APIRouter, Depends, status

from src.schemas.conta import conta_in, conta_in_edit
from src.views.conta import conta_out
from src.services import conta as services
from src.services.autenticacao import login_required

from typing import Annotated


router = APIRouter(prefix="/contas", tags=["Contas"])

@router.get("/", response_model=list[conta_out])
async def listar_contas(dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    return await services.listar_contas(dados_usuario_logado)

@router.get("/{conta_id}", response_model=conta_out)
async def obter_conta(conta_id: int, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    return await services.obter_conta(conta_id, dados_usuario_logado)

@router.get("/{conta_id}/saldo/", response_model=float)
async def exibir_saldo(conta_id: int, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    return await services.exibir_saldo(conta_id, dados_usuario_logado)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_conta(conta:conta_in, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    conta_id = await services.criar_conta(conta, dados_usuario_logado)
    return f"Criado conta ID {conta_id} com sucesso!"

@router.patch("/{conta_id}", status_code=status.HTTP_202_ACCEPTED)
async def editar_conta(conta_id:int, conta:conta_in_edit, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    await services.editar_conta(conta_id, conta, dados_usuario_logado)
    return f"Conta ID {conta_id} editada com sucesso!"

@router.delete("/{conta_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_conta(conta_id: int, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    await services.deletar_conta(conta_id, dados_usuario_logado)
    return
