from pydantic import AwareDatetime, BaseModel
from typing import Literal
from datetime import date

class ClienteIn(BaseModel):
    endereco: str

class ClienteInEdit(BaseModel):
    endereco: str | None = None

class PessoaFisicaIn(ClienteIn):
    tipo: str = Literal["pf"]
    cpf: str
    nome: str
    nascimento: date

class PessoaFisicaInEdit(ClienteInEdit):
    tipo: str = Literal["pf"]
    cpf: str | None = None
    nome: str | None = None
    nascimento: date | None = None

# Prevendo futuros tipos
class PessoaJuridicaIn(ClienteIn):
    tipo: str = Literal["pj"]
    cnpj: str
    razao_social: str

class PessoaJuridicaInEdit(ClienteInEdit):
    tipo: str = Literal["pj"]
    cnpf: str | None = None
    razao_social: str | None = None