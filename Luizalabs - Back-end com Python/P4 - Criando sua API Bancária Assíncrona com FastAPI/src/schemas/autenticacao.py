from pydantic import BaseModel

class AutenticacaoIn(BaseModel):
    cliente_id: int
    senha: str
