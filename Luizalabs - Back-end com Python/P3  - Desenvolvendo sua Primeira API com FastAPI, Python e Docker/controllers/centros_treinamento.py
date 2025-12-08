from fastapi import APIRouter

router = APIRouter(prefix="/centros_treinamento")

@router.get("/")
def consultar_centros_treinamento():
    return {"message": "Consultando centros de treinamento!"}

@router.post("/")
def criar_centro_treinamento():
    return {"message": "Criando centro de treinamento!"}

@router.get("/{id}")
def consultar_centro_treinamento_por_id():
    return {"message": "Consultando Centro de Treinamento por id!"}
