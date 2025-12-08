from fastapi import APIRouter

router = APIRouter(prefix="/atletas")

@router.post("/")
def criar_atleta():
    return {"message": "Criando Atleta!"}

@router.get("/")
def consultar_atletas():
    return {"message": "Consultando atletas!"}

@router.get("/{id}")
def consultar_atleta_por_id():
    return {"message": "Consultando Atleta por id!"}

@router.patch("/{id}")
def editar_atleta_por_id():
    return {"message": "Editando Atleta por id!"}

@router.delete("/{id}")
def consultar_atleta_por_id():
    return {"message": "Deletando Atleta por id!"}
