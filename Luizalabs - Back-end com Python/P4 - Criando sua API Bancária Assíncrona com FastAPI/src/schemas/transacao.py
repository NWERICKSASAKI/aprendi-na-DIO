from pydantic import BaseModel, AwareDatetime, Field
from typing import Literal

class TransacaoIn(BaseModel):
    transacao_id: int
    conta_id: int
    valor: float = Field(ge=0)
    tipo: Literal["s","d"]
    cadastrado_em: AwareDatetime

