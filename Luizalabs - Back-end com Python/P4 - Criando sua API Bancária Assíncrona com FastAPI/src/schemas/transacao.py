from pydantic import BaseModel, AwareDatetime

class TransacaoIn(BaseModel):
    transacao_id: int
    conta_id: int
    valor: float
    cadastrado_em: AwareDatetime

