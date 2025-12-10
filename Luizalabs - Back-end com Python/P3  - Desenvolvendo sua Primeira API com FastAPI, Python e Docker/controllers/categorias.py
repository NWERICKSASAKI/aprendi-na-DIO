from fastapi import APIRouter
from fastapi import status
from schemas.categorias import CategoriasIn

from services import categorias

core_router = APIRouter(prefix="/core/categorias")





orm_router = APIRouter(prefix="/orm/categorias")

@orm_router.get("/")
def consultar_categorias():
    return categorias.orm_get_all() 
    # return {"message": "Consultando categorias!"}

@orm_router.post("/", status_code=status.HTTP_201_CREATED)
def criar_categoria(post: CategoriasIn):
    categorias.orm_post(post)
    return {"message": post}

@orm_router.get("/{id}")
def consultar_categoria_por_id():
    return {"message": "Consultando Categoria por id!"}
