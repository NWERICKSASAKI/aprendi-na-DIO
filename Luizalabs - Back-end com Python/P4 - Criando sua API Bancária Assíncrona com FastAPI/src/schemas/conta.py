from pydantic import BaseModel, AwareDatetime

class ContaIn(BaseModel):
    conta_id: int # numero da conta
    agencia: str = "0001"
    # saldo: float # faz sentido ter saldo na criação da conta?
    cliente_id: int
    cadastrado_em: AwareDatetime

class ContaInEdit(BaseModel):
    conta_id: int | None = None
    agencia: str | None = None
    # saldo: float | None = None
    cliente_id: int | None = None
