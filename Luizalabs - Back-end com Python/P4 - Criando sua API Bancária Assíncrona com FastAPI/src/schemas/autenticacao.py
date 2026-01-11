from pydantic import BaseModel, Field
from typing import Optional
class AutenticacaoIn(BaseModel):
    cliente_id: int
    senha: str
    is_adm: Optional[bool] = Field(default=False) 
