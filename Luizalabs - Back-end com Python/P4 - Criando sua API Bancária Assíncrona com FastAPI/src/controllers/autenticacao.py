from fastapi import APIRouter

from src.schemas.autenticacao import AutenticacaoIn
from src.services import autenticacao
from src.views.autenticacao import AutenticacaoOut

router = APIRouter(prefix="/login", tags=["Autenticação"])

@router.post("/", response_model=AutenticacaoOut)
async def autenticar(credenciais: AutenticacaoIn):
    return autenticacao.autenticar(user_id = credenciais.user_id)

@router.patch("/", response_model=AutenticacaoOut)
async def alterar_senha(credenciais: AutenticacaoIn):
    return {"message": "Senha alterada com sucesso"}
