from pydantic import AwareDatetime, BaseModel, NaiveDatetime

class Cliente(BaseModel):
    cliente_id: int
    cpf: str
    nome: str
    nascimento: AwareDatetime | NaiveDatetime | None
    cadastrado_em: AwareDatetime | NaiveDatetime | None

class ClienteEdit(BaseModel):
    cliente_id: int | None = None
    cpf: str | None = None
    nome: str | None = None
    nascimento: AwareDatetime | NaiveDatetime | None = None
    cadastrado_em: AwareDatetime | NaiveDatetime | None = None