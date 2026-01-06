from pydantic import BaseModel, AwareDatetime

class TransacaoOut(BaseModel):
    id: int
    conta_id: int
    valor: float
    tipo: str
    com_sucesso: bool
    cadastrado_em: AwareDatetime
