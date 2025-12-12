from fastapi import APIRouter
from fastapi import status
from schemas.categorias import CategoriasIn

from services import categorias

core_router = APIRouter(prefix="/core/categorias")

@core_router.get("/")
def core_consultar_categorias():
    # return {"message": "Consultando categorias!"}
    return categorias.core_get_all() 

@core_router.post("/", status_code=status.HTTP_201_CREATED)
def core_criar_categoria(post: CategoriasIn):
    categorias.core_post(post)
    return {"message": post}

@core_router.get("/{id}")
def core_consultar_categoria_por_id(id: int):
    return categorias.core_get(id) 




orm_router = APIRouter(prefix="/orm/categorias")

@orm_router.get("/")
def orm_consultar_categorias():
    return categorias.orm_get_all() 
    # return {"message": "Consultando categorias!"}

@orm_router.post("/", status_code=status.HTTP_201_CREATED)
def orm_criar_categoria(post: CategoriasIn):
    categorias.orm_post(post)
    return {"message": post}

@orm_router.get("/{id}")
def orm_consultar_categoria_por_id(id:int):
    return categorias.orm_get(id)
