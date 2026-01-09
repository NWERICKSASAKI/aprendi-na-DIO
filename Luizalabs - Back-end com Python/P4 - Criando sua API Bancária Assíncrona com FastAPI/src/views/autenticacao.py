from pydantic import BaseModel

class AutenticacaoOut(BaseModel):
    hash_access_token: str

class AccessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str
