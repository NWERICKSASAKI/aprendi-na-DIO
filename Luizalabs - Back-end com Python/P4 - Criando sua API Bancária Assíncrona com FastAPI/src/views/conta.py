from pydantic import BaseModel, AwareDatetime, Field
from typing import Literal, Annotated, Union

class ContaOut(BaseModel):
    id: int
    saldo: float
    agencia: str
    cadastrado_em: AwareDatetime

class ContaCorrenteOut(ContaOut):
    tipo: Literal["cc"] = "cc"
    cc_id: int
    valor_saques: float
    limite: float
    qtd_saques: int
    limite_saque: int

class ContaEmpresarialOut(ContaOut):
    tipo: Literal["ce"] = "ce"
    ce_id: int
    emprestimo: float
    emprestimo_limite: float

conta_out = Annotated[
    Union[ContaCorrenteOut,ContaEmpresarialOut],
    Field(discriminator="tipo")
]
