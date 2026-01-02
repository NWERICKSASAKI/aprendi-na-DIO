from fastapi import APIRouter, Depends, status

from src.schemas.transacao import TransacaoIn
from src.views.transacao import TransacaoOut

# TODO adicionar dependencias de login
router = APIRouter(prefix="/transacao", tags=["Transação"])

@router.get("/")
#@router.get("/", response_model=list[TransacaoOut])
async def listar_transacoes():
    return "Listando todas as transações"

@router.get("/{transacao_id}")
#@router.get("/", response_model=list[TransacaoOut])
async def visualizar_transacao(transacao_id: int):
    return f"Listando transação {transacao_id}"

@router.get("/cliente/{cliente_id}")
#@router.get("/cliente/{cliente_id}", response_model=list[TransacaoOut])
async def visualizar_extrato_cliente(cliente_id: int):
    return f"Aqui está o seu extrato"

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
#@router.post("/", response_model=TransacaoOut, status_code=status.HTTP_202_ACCEPTED)
async def realizar_transacao(transacao:TransacaoIn):
    return f"Transacao realizada com sucesso no valor de {transacao.valor}"
