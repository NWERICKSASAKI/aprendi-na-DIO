from pydantic import BaseModel


class AutenticacaoOut(BaseModel):
    access_token: str
class JWTToken(BaseModel):
    access_token: AccessToken

class AccessToken(BaseModel):
    iss: str
    sub: int
    adm: bool
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str

