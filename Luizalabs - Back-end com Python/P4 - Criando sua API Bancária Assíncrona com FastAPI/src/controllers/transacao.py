from fastapi import APIRouter, Depends, status
from typing import Annotated

from src.schemas.transacao import TransacaoIn
from src.views.transacao import TransacaoOut
from src.services import transacao as services
from src.services.autenticacao import login_required

router = APIRouter(prefix="/transacao", tags=["Transação"])

@router.get("/", response_model=list[TransacaoOut])
async def listar_transacoes(dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    return await services.listar_transacoes(dados_usuario_logado)

@router.get("/{transacao_id}", response_model=TransacaoOut)
async def visualizar_transacao(transacao_id: int, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    return await services.visualizar_transacao(transacao_id, dados_usuario_logado)

@router.get("/cliente/{cliente_id}", response_model=list[TransacaoOut])
async def visualizar_extrato_cliente(cliente_id: int, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    return await services.visualizar_extrato_cliente(cliente_id, dados_usuario_logado)

@router.post("/sacar/", status_code=status.HTTP_202_ACCEPTED)
async def realizar_saque(transacao:TransacaoIn, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    id = await services.realizar_transacao(transacao, tipo_transacao="s", dados_usuario_logado=dados_usuario_logado)
    return f"Saque realizado! ID {id}"

@router.post("/depositar/", status_code=status.HTTP_202_ACCEPTED)
async def realizar_deposito(transacao:TransacaoIn, dados_usuario_logado: Annotated[dict, Depends(login_required)]):
    id = await services.realizar_transacao(transacao, tipo_transacao="d", dados_usuario_logado=dados_usuario_logado)
    return f"Deposito realizado com sucesso! ID {id}"
