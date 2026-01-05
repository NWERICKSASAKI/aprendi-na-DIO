from pydantic import BaseModel, Field
from typing import Literal

class ContaIn(BaseModel):
    numero_conta: int 
    agencia: str = "0001"

class ContaInEdit(BaseModel):
    numero_conta: int | None = None
    agencia: str | None = None

class ContaCorrenteIn(ContaIn):
    tipo: Literal["cc"] = "cc"
    limite: float = Field(ge=0)
    limites_saques: int = Field(ge=0)

class ContaCorrenteInEdit(ContaInEdit):
    tipo: str = Literal["cc"]
    limite: float | None = Field(default=None, ge=0)
    limites_saques: int | None = Field(default=None, ge=0)

class ContaEmpresarialIn(ContaIn):
    tipo: str = Literal["ce"]
    emprestimo: float = Field(ge=0)
    emprestimo_limite: float = Field(ge=0)

class ContaEmpresarialInEdit(ContaInEdit):
    tipo: str = Literal["ce"]
    emprestimo: float | None  = Field(default=None, ge=0)
    emprestimo_limite: float | None  = Field(default=None, ge=0)
    