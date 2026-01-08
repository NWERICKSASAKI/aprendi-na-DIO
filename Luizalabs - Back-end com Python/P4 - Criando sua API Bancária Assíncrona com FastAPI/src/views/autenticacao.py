from pydantic import BaseModel

class AutenticacaoOut(BaseModel):
    access_token: str

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