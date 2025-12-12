from fastapi import APIRouter
from schemas.centros_treinamento import CentrosTreinamentoIn
from services import centros_treinamento

core_router = APIRouter(prefix="/core/centros_treinamento")

@core_router.get("/")
def core_consultar_centros_treinamento():
    return centros_treinamento.core_get_all()

@core_router.post("/")
def core_criar_centro_treinamento(json_data: CentrosTreinamentoIn):
    centros_treinamento.core_post(json_data)    
    return {"message": f"Criando centro de treinamento: {json_data.nome}"}

@core_router.get("/{id}")
def core_consultar_centro_treinamento_por_id(id: int):
    return centros_treinamento.core_get(id)
    # return {"message": "Consultando Centro de Treinamento por id!"}



orm_router = APIRouter(prefix="/orm/centros_treinamento")
@orm_router.get("/")
def orm_consultar_centros_treinamento():
    return centros_treinamento.orm_get_all()

@orm_router.post("/")
def orm_criar_centro_treinamento(json_data: CentrosTreinamentoIn):
    centros_treinamento.orm_post(json_data)    
    return {"message": f"Criando centro de treinamento: {json_data.nome}"}

@orm_router.get("/{id}")
def orm_consultar_centro_treinamento_por_id(id:int):
    return centros_treinamento.orm_get(id)


