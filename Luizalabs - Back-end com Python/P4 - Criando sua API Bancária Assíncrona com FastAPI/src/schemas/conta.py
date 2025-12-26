from pydantic import BaseModel

class Conta(BaseModel):
    conta_id: int # numero da conta
    agencia: str
    saldo: float
    cliente_id: int

class ContasEdit(BaseModel):
    conta_id: int | None = None
    agencia: str | None = None
    saldo: float | None = None
    cliente_id: int | None = None