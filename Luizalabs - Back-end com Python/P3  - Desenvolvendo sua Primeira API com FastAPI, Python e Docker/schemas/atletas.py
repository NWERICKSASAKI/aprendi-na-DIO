from pydantic import BaseModel

class AtletasIn(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: int
    categoria_id: int