from fastapi import APIRouter
from database.create_db import create_db

router = APIRouter(prefix="/teste")

@router.get("/")
def teste_endpoint():   
    create_db()
    return {"message": "Teste endpoint funcionando!"}