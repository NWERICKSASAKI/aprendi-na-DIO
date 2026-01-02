from pydantic import AwareDatetime, BaseModel, NaiveDatetime
from datetime import date

class ClienteIn(BaseModel):
    # Cliente
    endereco: str
    # PessoaFisica
    cpf: str
    nome: str
    nascimento: date
    # etc
    cadastrado_em: AwareDatetime | None

class ClienteInEdit(BaseModel):
    # Cliente
    endereco: str | None = None
    # PessoaFisica
    cpf: str | None = None
    nome: str | None = None
    nascimento: date | None = None
