from pydantic import BaseModel, AwareDatetime, Field

class ContaIn(BaseModel):
    # id
    # saldo: float # faz sentido ter saldo na criação da conta?
    numero_conta: int 
    agencia: str = "0001"
    cliente_id: int
    historico_id: int
    cadastrado_em: AwareDatetime

class ContaInEdit(BaseModel):
    # id
    # saldo
    numero_conta: int | None = None
    agencia: str | None = None
    cliente_id: int | None = None
    historico_id: int | None = None
    # cadastrado_em: AwareDatetime

class ContaCorrente(BaseModel):
    # id: int
    conta_id: int
    limite: float = Field(ge=0)
    limites_saques: int = Field(ge=0)

class ContasCorrenteEdit(BaseModel):
    # id: int | None = None
    conta_id: int | None = None
    limite: float | None = None
    limites_saques: int | None = None
