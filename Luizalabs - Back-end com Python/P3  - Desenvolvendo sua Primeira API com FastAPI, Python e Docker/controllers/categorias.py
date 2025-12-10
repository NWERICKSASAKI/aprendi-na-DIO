from fastapi import APIRouter
from fastapi import status
from schemas.categorias import CategoriasIn

router = APIRouter(prefix="/categorias")

@router.get("/")
def consultar_categorias():
    return {"message": "Consultando categorias!"}

@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_categoria(post: CategoriasIn):
    return {"message": post}

@router.get("/{id}")
def consultar_categoria_por_id():
    return {"message": "Consultando Categoria por id!"}
