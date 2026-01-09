from fastapi import APIRouter, Depends

from src.schemas.autenticacao import AutenticacaoIn
from src.services import autenticacao
from src.views.autenticacao import AutenticacaoOut

from typing import Annotated

router = APIRouter(prefix="/login", tags=["Autenticação"])

@router.post("/", response_model=AutenticacaoOut)
async def autenticar(credenciais: AutenticacaoIn):
    return await autenticacao.autenticar(credenciais)

@router.patch("/")
async def alterar_senha(credenciais: AutenticacaoIn, id_cliente_logado: Annotated[int, Depends(autenticacao.login_required)]):
    return await autenticacao.alterar_senha(credenciais, id_cliente_logado)
