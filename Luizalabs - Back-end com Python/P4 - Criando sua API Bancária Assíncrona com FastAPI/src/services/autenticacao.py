import jwt
import time
from typing import Annotated
from uuid import uuid4
from fastapi import Depends, Request
from fastapi.security import HTTPBearer
import sqlalchemy as sa
from src import exceptions
from src.views import autenticacao
from src.config import settings
from src.models.autenticacao import autenticacao as autenticacao_table
from src.database import database


async def _comparar_usuario_senha(credenciais_json) -> bool:
    input_cliente_id = credenciais_json.cliente_id
    input_senha = credenciais_json.senha
    query = sa.select(autenticacao_table.c.senha).where(autenticacao_table.c.cliente_id == input_cliente_id)
    senha_armazenada = await database.fetch_one(query)
    if input_senha == senha_armazenada['senha']:
        return True
    return False


async def autenticar(credenciais_json) -> autenticacao.AutenticacaoOut | None:
    if await _comparar_usuario_senha(credenciais_json):
        return _gerar_token(credenciais_json.cliente_id)
    raise exceptions.Error_401_UNAUTHORIZED("Senha inválida")


def _gerar_token(user_id: int) -> autenticacao.AutenticacaoOut:
    now = time.time()
    payload = {
        "iss": "aprendi_na_dio",
        "sub": str(user_id),
        "aud": "projeto_sistema_bancario",
        "exp": now + (60 * 30),
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }
    token = jwt.encode(payload, settings.secret, algorithm=settings.algorithm)
    return {"hash_access_token": token}


async def _descondificar_token(token: str) -> autenticacao.AutenticacaoOut | None:
    try:
        decoded_token = jwt.decode(
            token,
            settings.secret,
            [settings.algorithm],
            audience="projeto_sistema_bancario",
        )
        _token = autenticacao.AutenticacaoOut.model_validate({"access_token": decoded_token})
        return _token if _token.hash_access_token.exp >= time.time() else None
    except:
        return None

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error:bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> autenticacao.AutenticacaoOut:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")

        if credentials:
            if not scheme == "Bearer":
                raise exceptions.Error_401_UNAUTHORIZED("invalid authorizarion scheme.")
            
            payload = await _descondificar_token(credentials)
            if not payload:
                raise exceptions.Error_401_UNAUTHORIZED(f"invalid or expired token: {payload}")
            return payload
        else:
            raise exceptions.Error_401_UNAUTHORIZED("invalid authorizarion code.")


async def _get_current_user(token: Annotated[autenticacao.AutenticacaoOut, Depends(JWTBearer())]) -> int:
    cliente_id = token.hash_access_token.sub # sub é o user id
    return cliente_id


def login_required(current_user: Annotated[int, Depends(_get_current_user)]) -> int:
    if not current_user: # caso nao tiver user_id
        raise exceptions.Error_403_FORBIDDEN("access denied")
    return current_user


async def criar_senha(cliente_id, senha) -> int:
    query = autenticacao_table.insert().values(
        cliente_id = cliente_id,
        senha = senha
    )
    id = await database.execute(query)
    return id


async def alterar_senha(credenciais_json, id_cliente_logado: Annotated[int, Depends(autenticacao.login_required)]):
    if id_cliente_logado == credenciais_json.cliente_id:
        query = autenticacao_table.update().values(credenciais_json.model_dump()).where(autenticacao_table.c.id == credenciais_json.cliente_id)
        result = await database.execute(query)
        return f"Senha alterada com sucesso!"
    raise exceptions.Error_403_FORBIDDEN("Você não pode alterar senha de outros usuários!")

