from pydantic import BaseModel, AwareDatetime

class ContaOut(BaseModel):
    id: int  # numero da conta
    saldo: float
    numero_conta: int  # numero da conta
    agencia: str
    cliente_id: int
    historico_id: int
    cadastrado_em: AwareDatetime
    limite: float
    limite_saques: int