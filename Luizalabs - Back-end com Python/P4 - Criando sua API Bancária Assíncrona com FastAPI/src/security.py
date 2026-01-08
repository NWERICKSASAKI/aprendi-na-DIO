# import time
# from typing import Annotated
# from uuid import uuid4

# import jwt
# from fastapi import Depends, HTTPException, Request, status
# from fastapi.security import HTTPBearer
# from pydantic import BaseModel

# SECRET = "my-secret"
# ALGORITHM = "HS256"

# class AccessToken(BaseModel):
#     iss: str
#     sub: int
#     aud: str
#     exp: float
#     iat: float
#     nbf: float
#     jti: str

# class JWTToken(BaseModel):
#     access_token: AccessToken

# def sign_jwt(user_id: int) -> JWTToken:
#     now = time.time()
#     payload = {
#         "iss": "curso-fastapi.com.br",
#         "sub": user_id,
#         "aud": "curso-fastapi",
#         "exp": now + (60 * 30), # 30min
#         "iat": now,
#         "nbf": now,
#         "jti": uuid4().hex,
#     }
#     token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
#     return {"access_token": token}

# async def decode_jwt(token: str) -> JWTToken | None:
#     # recebe o valor do token (codificado)
#     try:
#         decoded_token = jwt.decode(
#             token,
#             SECRET,
#             audience="curso-fastapi",
#             algorithm=[ALGORITHM]
#         )
#         _token = JWTToken.model_validate({"access_token": decoded_token})
#         return _token if _token.access_token.exp >= time.time() else None
#     except Exception:
#         return None

# class JWTBearer(HTTPBearer):
#     def __init__(self, auto_error:bool = True):
#         super(JWTBearer, self).__init__(auto_error=auto_error)

#     # esse __call__ é pra sobrescrever o comportamento do Bearer
#     # pq quando não tem autorização retornar ERRO 403
#     # mas o 403 é pra quando o usuario tá autenticado mas não tem autorização
#     async def __call__(self, request: Request) -> JWTToken:
#         authorization = request.headers.get("Authorization", "")
#         scheme, _, credentials = authorization.partition(" ")

#         if credentials:
#             if not scheme == "Bearer":
#                 raise HTTPException(
#                     status_code=status.HTTP_401_UNAUTHORIZED,
#                     detail="invalid authorizarion scheme."
#                 )
            
#             payload = await decode_jwt(credentials)
#             if not payload:
#                 raise HTTPException(
#                     status_code=status.HTTP_401_UNAUTHORIZED,
#                     detail="invalid or expired token."
#                 )
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="invalid authorizarion code."
#             )
            
# async def get_current_user(token: Annotated[JWTToken, Depends(JWTBearer())]) -> dict[str, int]:
#     return {"user_id": token.access_token.sub} # sub é o user id

# def login_required(current_user: Annotated[dict[str, int], Depends(get_current_user)]):
#     if not current_user: # caso nao tiver user_id
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
#     return current_user
