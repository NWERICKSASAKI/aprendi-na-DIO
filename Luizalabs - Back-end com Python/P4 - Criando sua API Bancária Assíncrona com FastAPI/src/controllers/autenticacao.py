from fastapi import APIRouter, Depends, status, Request
from fastapi.templating import Jinja2Templates

from http import HTTPStatus

from src.schemas.autenticacao import AutenticacaoIn
from src.services import autenticacao
from src.views.autenticacao import AutenticacaoOut

from typing import Annotated

router = APIRouter(prefix="/login", tags=["Autenticação"])




templates = Jinja2Templates(directory="frontend/templates")


@router.get("/login")
async def page_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/", response_model=AutenticacaoOut, status_code=status.HTTP_200_OK)
async def autenticar(credenciais: AutenticacaoIn):
    return await autenticacao.autenticar(credenciais.model_dump())

@router.patch("/", status_code=status.HTTP_202_ACCEPTED)
async def alterar_senha(credenciais: AutenticacaoIn, dados_usuario_logado: Annotated[dict, Depends(autenticacao.login_required)]):
    return await autenticacao.alterar_senha(credenciais.model_dump(), dados_usuario_logado)
