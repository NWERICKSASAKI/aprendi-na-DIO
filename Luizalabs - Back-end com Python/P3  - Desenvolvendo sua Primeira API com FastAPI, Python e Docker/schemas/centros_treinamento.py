from pydantic import BaseModel

class CentrosTreinamentoIn(BaseModel):
    nome: str
    endereco: str
    proprietario: str