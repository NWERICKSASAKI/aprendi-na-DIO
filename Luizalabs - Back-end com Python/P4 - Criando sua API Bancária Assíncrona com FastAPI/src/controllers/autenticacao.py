from fastapi import APIRouter

from src.schemas.autenticacao import AutenticacaoIn
# from src.security import sign_jwt
from src.views.autenticacao import AutenticacaoOut

router = APIRouter(prefix="/login", tags=["Autenticação"])

@router.post("/", response_model=AutenticacaoOut)
async def autenticar(credenciais: AutenticacaoIn):
    return {"message": "Autenticação bem-sucedida"}

@router.patch("/", response_model=AutenticacaoOut)
async def alterar_senha(credenciais: AutenticacaoIn):
    return {"message": "Senha alterada com sucesso"}
    # return sign_jwt(user_id = credenciais.user_id) TODO