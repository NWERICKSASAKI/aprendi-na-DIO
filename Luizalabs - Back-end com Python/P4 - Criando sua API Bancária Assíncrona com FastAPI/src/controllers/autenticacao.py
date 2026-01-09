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
async def alterar_senha(credenciais: AutenticacaoIn, dados_usuario_logado: Annotated[dict, Depends(autenticacao.login_required)]):
    return await autenticacao.alterar_senha(credenciais, dados_usuario_logado)
