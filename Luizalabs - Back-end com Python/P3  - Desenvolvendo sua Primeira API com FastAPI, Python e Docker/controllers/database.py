from fastapi import APIRouter
from database.connection import core_create_db, orm_create_db, engine
import os

core_router = APIRouter(prefix="/core/database")

@core_router.post("/")
def criar_bd_core():   
    core_create_db()
    return {"message": "Criando banco com CORE!"}

orm_router = APIRouter(prefix="/orm/database")

@orm_router.post("/")
def criar_bd_orm():   
    orm_create_db()
    return {"message": "Criando banco com ORM!"}

router = APIRouter(prefix="/database")

@router.delete("/")
def deletar_bd():   
    engine.dispose()
    os.remove("database/workout.db")
    return {"message": "Banco de dados deletado!"}
