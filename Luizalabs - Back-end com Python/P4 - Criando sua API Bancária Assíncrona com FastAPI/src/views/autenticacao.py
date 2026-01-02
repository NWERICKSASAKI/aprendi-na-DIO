from pydantic import BaseModel

class AutenticacaoOut(BaseModel):
    access_token: str
