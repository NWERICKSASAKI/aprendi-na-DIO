from pydantic import BaseModel, AwareDatetime, Field
from typing import Literal

class ContaIn(BaseModel):
    numero_conta: int 
    agencia: str = "0001"
    cliente_id: int
    historico_id: int
    cadastrado_em: AwareDatetime

class ContaInEdit(BaseModel):
    numero_conta: int | None = None
    agencia: str | None = None
    cliente_id: int | None = None
    historico_id: int | None = None

class ContaCorrenteIn(ContaIn):
    conta_id: int
    tipo: Literal["cc"] = "cc"
    limite: float = Field(ge=0)
    limites_saques: int = Field(ge=0)

class ContaCorrenteInEdit(ContaInEdit):
    tipo: str = Literal["cc"]
    limite: float | None = None
    limites_saques: int | None = None

class ContaEmpresarialIn(ContaIn):
    conta_id: int
    tipo: str = Literal["ce"]
    emprestimo: float = Field(ge=0)
    emprestimo_limite: float = Field(ge=0)

class ContaEmpresarialInEdit(ContaInEdit):
    # conta_id: int | None = None
    tipo: str = Literal["ce"]
    emprestimo: float | None  = Field(default=None, ge=0)
    emprestimo_limite: float | None  = Field(default=None, ge=0)
    