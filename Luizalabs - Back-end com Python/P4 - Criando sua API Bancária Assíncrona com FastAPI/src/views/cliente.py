from pydantic import BaseModel, AwareDatetime, Field
from datetime import date
from typing import Literal, Annotated, Union


class ClienteOut(BaseModel):
    id: int
    endereco: str
    contas_id: list[int] | None
    cadastrado_em: AwareDatetime

class PessoaFisicaOut(ClienteOut):
    tipo: Literal["pf"] = "pf"
    pf_id: int
    cpf: str
    nome: str
    nascimento: date

class PessoaJuridicaOut(ClienteOut):
    tipo: Literal["pj"] = "pj"
    pj_id: int
    cnpj: str
    razao_social: str


cliente_out = Annotated[
    Union[PessoaFisicaOut, PessoaJuridicaOut],
    Field(discriminator="tipo")
]
