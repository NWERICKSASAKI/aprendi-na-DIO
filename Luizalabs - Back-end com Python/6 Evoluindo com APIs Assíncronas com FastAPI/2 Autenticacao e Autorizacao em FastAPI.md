# 2 Autenticação e Autorização em FastAPI

## Como iremos autenticar as nossas rotas

Para proteger as end-points para acesso indevidos por tokens.
Quando acessar a end-point sem o token retornar Autorização inválida e não executar o end-point.

## Uso de tokens para autenticação

`auth.py`:
```py
from fastapi import APIRouter

from schemas.auth import LoginIn
from security import sign_jwt
from views.auth import LoginOut

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginOut)
async def login(data: LoginIn):
    return sign_jwt(user_id=data.user_id)
```

`schemas/auth.py`:
```py
from pydantic import BaseModel

# por enquanto não vamos buscar/comparar senha, só usuário
class LoginIn(BaseModel):
    user_id: int
```

`views/auth.py`:
```py
from pydantic import BaseModel

class LoginOut(BaseModel):
    access_token: str
```

`security.py`:
```py
import tim
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.secutiry import HTTPBearer
from pydantic import BaseModel

SECRET = "my-secret"
ALGORITHM = "HS256"

class AccessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str

class JWTToken(BaseModel):
    access_token: AccessToken

def sign_jwt(user_id: int) -> JWTToken:
    now = time.time()
    payload = {
        "iss": "curso-fastapi.com.br",
        "sub": user_id,
        "aud": "curso-fastapi",
        "exp": now + (60 * 30), # 30min
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return {"access_token": token}

async def decode_jwt(token: str) -> JWTToken | None:
    # recebe o valor do token (codificado)
    try:
        decoded_token = jwt.decode(
            token,
            SECRET,
            audience="curso-fastapi",
            algorithm=[ALGORITHM]
        )
        _token = JWTToken.model_validate({"access_token": decoded_token})
        return _token if _token.access_token.exp >= time.time() else None
    except Exception:
        return None

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error:bool = True)
        super(JWTBearer, self).__init__(auto_error=auto_error)

    # esse __call__ é pra sobrescrever o comportamento do Bearer
    # pq quando não tem autorização retornar ERRO 403
    # mas o 403 é pra quando o usuario tá autenticado mas não tem autorização
    async def __call__(self, request: Request) -> JWTToken:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")

        if credentials:
            if not scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="invalid authorizarion scheme."
                )
            
            payload = await.decode_jwt(credentials)
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
            
async def get_current_user(token: Annotated[JWTToken, Depends(JWTBearer())]) -> dict[str, int]:
    return {"user_id": token.access_token.sub} # sub é o user id

def login_required(current_user: Annotated[dict[str, int], Dedends(get_current_user)]):
    if not current_user: # caso nao tiver user_id
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    return current_user

```

`main.py`:
```py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from controllers import post
from database import database, engine, metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield 
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.include_router(post.router)
```
  
  
`controllers/post.py`:
```py
from fastapi import APIRouter, Depends, status

from schemas.post import PostIn, PostUpdateIn
from security import login_required
from services.post import PostService
from views.post import PostOut

router = APIRouter(prefix="/post", dependencies=[Depends(login_required)])
# dependencia pode pedir dados vir por header / parameter

service = PostService()

# daria pra passar individualmente o arg: dependencies=[Depends(login_required)]
@router.get("/", response_model=list[PostOut]) 
async def read_posts(published:bool, limit:int, skip:int = 0):
    return await service.read_all(published=published, limit=limit, skip=skip)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    return {**post.model_dump(), "id": await service.create(post)}

@router.get("/{id}",response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)

@router.patch("/{id}",response_model=PostOut)
async def update_post(id: int):
    return await service.update(id=id, post=post)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=PostOut)
async def delete_post(id: int):
    await service.delete(id=id)
```

No Insonia, ir no método de autenticação e selecionar `Bearer Token`:
* `ENABLED`,
* `TOKEN` você pode digitar `response` e selecionar `body attribute`, clica nele vermelho e na opção de `Request` selecionar `[Auth] POST login` e em `Filter (JSONPath or XPATH)` = `$.access_token` e em `Trigger Behavior` marca `Always - resend request when needed`,
* `PREFIX` = `Bearer`

Precisa da biblioteca -> `poetry add "pyjwt"`
