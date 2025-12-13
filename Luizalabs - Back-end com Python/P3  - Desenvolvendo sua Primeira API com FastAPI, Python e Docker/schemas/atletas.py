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

class AtletasEdit(BaseModel):
    nome: str | None = None
    cpf: str | None = None
    idade: int | None = None
    peso: float | None = None
    altura: float | None = None
    sexo: str | None = None
    centro_treinamento_id: int | None = None
    categoria_id: int | None = None