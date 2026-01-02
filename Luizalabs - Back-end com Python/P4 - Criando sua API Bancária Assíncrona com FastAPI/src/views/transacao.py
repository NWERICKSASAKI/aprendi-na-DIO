from pydantic import BaseModel, AwareDatetime

class TransacaoOut(BaseModel):
    id: int
    conta_id: int
    valor: float
    tipo: str
    cadastrado_em: AwareDatetime
    