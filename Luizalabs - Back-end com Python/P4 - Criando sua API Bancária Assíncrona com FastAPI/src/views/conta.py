from pydantic import BaseModel, AwareDatetime
from typing import Literal

class ContaOut(BaseModel):
    id: int
    saldo: float
    numero_conta: int 
    agencia: str
    cadastrado_em: AwareDatetime

class ContaCorrenteOut(ContaOut):
    tipo: Literal["cc"] = "cc"
    cc_id: int
    limite: float
    limite_saques: int

class ContaEmpresarialOut(ContaOut):
    tipo: Literal["ce"] = "ce"
    ce_id: int
    emprestimo: float
    emprestimo_limite: float
