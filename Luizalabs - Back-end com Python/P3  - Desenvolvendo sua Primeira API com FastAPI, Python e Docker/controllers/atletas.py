from fastapi import APIRouter
from services import atletas
from schemas.atletas import AtletasIn

core_router = APIRouter(prefix="/core/atletas")

@core_router.post("/")
def criar_atleta(json_data: AtletasIn):
    atletas.core_post(json_data)
    return {"message": f"Atleta! {json_data.nome} criado com sucesso."}

@core_router.get("/")
def consultar_atletas():
    return atletas.core_get_all()

@core_router.get("/{id}")
def consultar_atleta_por_id(id: int):
    return atletas.core_get(id)

@core_router.patch("/{id}")
def editar_atleta_por_id(json_data: AtletasIn, id: int):
    return {"message": "Editando Atleta por id!"}

@core_router.delete("/{id}")
def consultar_atleta_por_id(id: int):
    atletas.core_delete(id)
    return {"message": f"Deletando Atleta do {id} !"}


orm_router = APIRouter(prefix="/orm/atletas")

@orm_router.post("/")
def criar_atleta(json_data: AtletasIn):
    atletas.orm_post(json_data)
    return {"message": f"Atleta {json_data.nome} criado!"}

@orm_router.get("/")
def consultar_atletas():
    return atletas.orm_get_all()

@orm_router.get("/{id}")
def consultar_atleta_por_id(id: int):
    return atletas.orm_get(id)

@orm_router.patch("/{id}")
def editar_atleta_por_id(id: int):
    return {"message": "Editando Atleta por id!"}

@orm_router.delete("/{id}")
def consultar_atleta_por_id(id: int):
    atletas.orm_delete(id)
    return {"message": f"Deletando Atleta do id {id} !"}
