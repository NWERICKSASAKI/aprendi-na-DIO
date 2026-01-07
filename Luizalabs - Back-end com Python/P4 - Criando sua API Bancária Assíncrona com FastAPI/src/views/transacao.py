from pydantic import BaseModel, AwareDatetime
from typing import Literal
class TransacaoOut(BaseModel):
    id: int
    conta_id: int
    valor: float
    tipo: Literal["d","s"]
    com_sucesso: bool
    cadastrado_em: AwareDatetime
