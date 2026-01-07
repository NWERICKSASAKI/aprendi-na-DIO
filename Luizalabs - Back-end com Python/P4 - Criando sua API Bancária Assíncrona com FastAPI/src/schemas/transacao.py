from pydantic import BaseModel, AwareDatetime, Field
from typing import Literal

class TransacaoIn(BaseModel):
    conta_id: int
    valor: float = Field(ge=0)
