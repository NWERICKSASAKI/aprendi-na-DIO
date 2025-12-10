from fastapi import APIRouter
from database.connection import core_create_db, orm_create_db, engine
import os

router = APIRouter(prefix="/database")

@router.post("/core")
def criar_bd_core():   
    core_create_db()
    return {"message": "Criando banco com CORE!"}

@router.post("/orm")
def criar_bd_orm():   
    orm_create_db()
    return {"message": "Criando banco com ORM!"}

@router.delete("/")
def deletar_bd():   
    engine.dispose()
    os.remove("database/workout.db")
    return {"message": "Banco de dados deletado!"}
