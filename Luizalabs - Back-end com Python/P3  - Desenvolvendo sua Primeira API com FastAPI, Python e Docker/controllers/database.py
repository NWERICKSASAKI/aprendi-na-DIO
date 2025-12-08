from fastapi import APIRouter
from database.connection import create_core_db, create_orm_db
import os

router = APIRouter(prefix="/database")

@router.post("/core")
def criar_bd_core():   
    create_core_db()
    return {"message": "Criando banco com CORE!"}

@router.post("/orm")
def criar_bd_orm():   
    create_orm_db()
    return {"message": "Criando banco com ORM!"}

@router.delete("/")
def deletar_bd():   
    os.remove("database/workout.db")
    return {"message": "Banco de dados deletado!"}
