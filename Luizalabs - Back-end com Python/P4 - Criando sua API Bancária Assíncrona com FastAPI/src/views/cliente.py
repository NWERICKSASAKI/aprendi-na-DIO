from pydantic import BaseModel, AwareDatetime, NaiveDatetime 
from datetime import date

class ClienteOut(BaseModel):
    cliente_id: int
    # Cliente
    endereco: str
    contas: list[dict] | None
    # PessoaFisica
    cpf: str
    nome: str
    nascimento: date
    # etc
    cadastrado_em: AwareDatetime | NaiveDatetime
