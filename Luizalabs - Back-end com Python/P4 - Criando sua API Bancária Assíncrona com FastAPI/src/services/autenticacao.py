import jwt
import time
from typing import Annotated
from uuid import uuid4
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from src.views import autenticacao
from src.config import settings
from src.models import autenticacao as autenticacao_models
from src.database import database


async def _comparar_usuario_senha(credenciais_json) -> bool:
    input_cliente_id = credenciais_json["cliente_id"]
    input_senha = credenciais_json["senha"]
    query = autenticacao_models.select(autenticacao_models.c.senha).where(autenticacao_models.c.cliente_id == input_cliente_id)
    senha_armazenada = await database.execute(query)
    if input_senha == senha_armazenada:
        return True
    return False


async def autenticar(credenciais_json) -> autenticacao.JWTToken | None:
    if await _comparar_usuario_senha(credenciais_json):
        return _gerar_token(credenciais_json["id"])
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid authorizarion code."
    )

def _gerar_token(user_id: int) -> autenticacao.JWTToken:
    now = time.time()
    payload = {
        "iss": "aprendi_na_dio",
        "sub": user_id,
        "aud": "projeto_sistema_bancario",
        "exp": now + (60 * 30), # 30min
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }
    token = jwt.encode(payload, settings.secret, algorithm=settings.algorithm)
    return {"access_token": token}


async def _descondificar_token(token: str) -> autenticacao.JWTToken | None:
    # recebe o valor do token (codificado)
    try:
        decoded_token = jwt.decode(
            token,
            settings.algorithm,
            audience="projeto_sistema_bancario",
            algorithm=[settings.algorithm]
        )
        _token = autenticacao.JWTToken.model_validate({"access_token": decoded_token})
        return _token if _token.access_token.exp >= time.time() else None
    except Exception:
        return None

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error:bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    # esse __call__ é pra sobrescrever o comportamento do Bearer
    # pq quando não tem autorização retornar ERRO 403
    # mas o 403 é pra quando o usuario tá autenticado mas não tem autorização
    async def __call__(self, request: Request) -> autenticacao.JWTToken:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")

        if credentials:
            if not scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="invalid authorizarion scheme."
                )
            
            payload = await _descondificar_token(credentials)
            if not payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="invalid or expired token."
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid authorizarion code."
            )
            

async def get_current_user(token: Annotated[autenticacao.JWTToken, Depends(JWTBearer())]) -> dict[str, int]:
    return {"user_id": token.access_token.sub} # sub é o user id


def login_required(current_user: Annotated[dict[str, int], Depends(get_current_user)]):
    if not current_user: # caso nao tiver user_id
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    return current_user
