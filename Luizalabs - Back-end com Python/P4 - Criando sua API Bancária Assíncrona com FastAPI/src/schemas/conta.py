from pydantic import BaseModel, Field
from typing import Literal, Union

class ContaIn(BaseModel):
    cliente_id: int
    agencia: str = "0001"

class ContaInEdit(BaseModel):
    cliente_id: int | None = None
    agencia: str | None = None

class ContaCorrenteIn(ContaIn):
    tipo: Literal["cc"] = "cc"
    limite: float = Field(ge=0)
    limite_saque: int = Field(ge=0)

class ContaCorrenteInEdit(ContaInEdit):
    tipo: str = Literal["cc"]
    limite: float | None = Field(default=None, ge=0)
    limite_saque: int | None = Field(default=None, ge=0)

class ContaEmpresarialIn(ContaIn):
    tipo: str = Literal["ce"]
    emprestimo_limite: float = Field(ge=0)

class ContaEmpresarialInEdit(ContaInEdit):
    tipo: str = Literal["ce"]
    # emprestimo: float | None  = Field(default=None, ge=0)
    emprestimo_limite: float | None  = Field(default=None, ge=0)


conta_in = Union[ContaCorrenteIn,ContaEmpresarialIn]
conta_in_edit = Union[ContaCorrenteInEdit,ContaEmpresarialInEdit]
