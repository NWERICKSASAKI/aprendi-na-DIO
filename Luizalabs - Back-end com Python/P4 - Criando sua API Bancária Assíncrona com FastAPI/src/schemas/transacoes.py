from pydantic import BaseModel

class Transacoes(BaseModel):
    id: int
    conta_id: int
    valor: float
    tipo: int

class TransacoesEdit(BaseModel):
    id: int | None = None
    conta_id: int | None = None
    valor: float | None = None
    tipo: int | None = None
