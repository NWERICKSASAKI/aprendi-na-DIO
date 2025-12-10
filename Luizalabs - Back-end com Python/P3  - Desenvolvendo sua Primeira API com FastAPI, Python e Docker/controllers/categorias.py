from fastapi import APIRouter
from fastapi import status
from schemas.categorias import CategoriasIn

from services import categorias

router = APIRouter(prefix="/categorias")

@router.get("/")
def consultar_categorias():
    return categorias.core_get_all() 
    # return {"message": "Consultando categorias!"}

@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_categoria(post: CategoriasIn):
    categorias.orm_post(post)
    return {"message": post}

@router.get("/{id}")
def consultar_categoria_por_id():
    return {"message": "Consultando Categoria por id!"}
