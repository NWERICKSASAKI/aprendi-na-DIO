from pydantic import BaseModel

class ContaCorrente(BaseModel):
    conta_id: int
    limite: float
    limites_saques: int

class ContasCorrenteEdit(BaseModel):
    conta_id: int | None = None
    limite: float | None = None
    limites_saques: int | None = None
