from fastapi import APIRouter

router = APIRouter(prefix="/categorias")

@router.get("/")
def consultar_categorias():
    return {"message": "Consultando categorias!"}

@router.post("/")
def criar_categoria():
    return {"message": "Criando categoria!"}

@router.get("/{id}")
def consultar_categoria_por_id():
    return {"message": "Consultando Categoria por id!"}
