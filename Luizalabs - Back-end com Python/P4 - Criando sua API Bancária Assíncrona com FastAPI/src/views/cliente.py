from pydantic import BaseModel, AwareDatetime
from datetime import date
from typing import Literal

class ClienteOut(BaseModel):
    id: int
    endereco: str
    # contas_id: list[dict] | None
    cadastrado_em: AwareDatetime

class PessoaFisicaOut(ClienteOut):
    cpf: str
    nome: str
    nascimento: date

class PessoaJuridicaOut(ClienteOut):
    cpnj: str
    razao_social: str
