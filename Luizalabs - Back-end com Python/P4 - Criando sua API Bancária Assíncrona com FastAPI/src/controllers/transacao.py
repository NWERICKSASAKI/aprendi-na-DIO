from fastapi import APIRouter, Depends, status

from src.schemas.transacao import TransacaoIn
from src.views.transacao import TransacaoOut
from src.services import transacao as services

router = APIRouter(prefix="/transacao", tags=["Transação"])

@router.get("/", response_model=list[TransacaoOut])
async def listar_transacoes():
    return await services.listar_transacoes()

@router.get("/{transacao_id}", response_model=TransacaoOut)
async def visualizar_transacao(transacao_id: int):
    return await services.visualizar_transacao(transacao_id)

@router.get("/cliente/{cliente_id}", response_model=list[TransacaoOut])
async def visualizar_extrato_cliente(cliente_id: int):
    return await services.visualizar_extrato_cliente(cliente_id)

@router.post("/conta/{conta_id}/sacar", response_model=TransacaoOut, status_code=status.HTTP_202_ACCEPTED)
async def realizar_saque(transacao:TransacaoIn):
    return await services.realizar_saque(transacao)

@router.post("/conta/{conta_id}/depositar", response_model=TransacaoOut, status_code=status.HTTP_202_ACCEPTED)
async def realizar_deposito(transacao:TransacaoIn):
    return await services.realizar_deposito(transacao)
