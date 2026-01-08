from pydantic import BaseModel
from typing import Literal
from datetime import date

class ClienteIn(BaseModel):
    endereco: str
    senha: str

class ClienteInEdit(BaseModel):
    endereco: str | None = None
    senha: str

class PessoaFisicaIn(ClienteIn):
    tipo: Literal["pf"] = "pf"
    cpf: str
    nome: str
    nascimento: date

class PessoaFisicaInEdit(ClienteInEdit):
    tipo: Literal["pf"] = "pf"
    cpf: str | None = None
    nome: str | None = None
    nascimento: date | None = None

# Prevendo futuros tipos
class PessoaJuridicaIn(ClienteIn):
    tipo: Literal["pj"] = "pj"
    cnpj: str
    razao_social: str

class PessoaJuridicaInEdit(ClienteInEdit):
    tipo: Literal["pj"] = "pj"
    cnpf: str | None = None
    razao_social: str | None = None
    