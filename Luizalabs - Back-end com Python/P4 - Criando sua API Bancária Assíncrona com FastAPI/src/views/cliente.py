from pydantic import BaseModel, AwareDatetime, NaiveDatetime 
from datetime import date

class ClienteOut(BaseModel):
    id: int
    endereco: str
    contas_id: list[dict] | None
    cadastrado_em: AwareDatetime | NaiveDatetime

class PessoaFisicaOut(ClienteOut):
    cpf: str
    nome: str
    nascimento: date

class PessoaJuridicaOut(ClienteOut):
    cpnj: str
    razao_social: str
