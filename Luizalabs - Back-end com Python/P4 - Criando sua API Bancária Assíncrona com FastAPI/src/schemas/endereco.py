from pydantic import BaseModel

class Endereco(BaseModel):
    conta_id: int
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    uf: str

class EnderecoEdit(BaseModel):
    conta_id: int | None = None
    logradouro: str | None = None
    numero: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    uf: str | None = None