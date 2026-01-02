from pydantic import BaseModel

class ContaOut(BaseModel):
    conta_id: int  # numero da conta
    agencia: str
    saldo: float
    cliente_id: int
    limite: float
    limite_saques: int
