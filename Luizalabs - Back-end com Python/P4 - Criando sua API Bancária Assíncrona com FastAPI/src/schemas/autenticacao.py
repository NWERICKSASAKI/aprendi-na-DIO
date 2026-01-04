from pydantic import AwareDatetime, BaseModel, NaiveDatetime

class AutenticacaoIn(BaseModel):
    cliente_id: int
    senha: str
