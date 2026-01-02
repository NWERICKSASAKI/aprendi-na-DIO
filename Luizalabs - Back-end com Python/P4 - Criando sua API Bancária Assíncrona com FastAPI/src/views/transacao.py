from pydantic import BaseModel, AwareDatetime, NaiveDatetime

class TransacaoOut(BaseModel):
    transacao_id: int
    conta_id: int
    valor: float
    cadastrado_em: AwareDatetime | NaiveDatetime