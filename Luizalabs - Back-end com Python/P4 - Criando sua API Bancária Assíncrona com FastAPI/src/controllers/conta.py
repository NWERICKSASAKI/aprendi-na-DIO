from fastapi import APIRouter, Depends, status

from src.schemas.conta import ContaIn, ContaInEdit
from src.views.conta import ContaOut
from src.views.transacao import TransacaoOut

router = APIRouter(prefix="/contas", tags=["Contas"])

@router.get("/")
# @router.get("/", response_model=list[ContaOut])
async def listar_contas():
    return "Lista de contas"  # TODO implementar lógica de listagem de clientes

@router.get("/{id_conta}")
# @router.get("/{id_conta}", response_model=ContaOut)
async def exibir_conta(id_conta: int):
    return f"Exibindo os dados da conta {id_conta}"

@router.get("/{id_conta}/saldo/", response_model=float)
async def exibir_saldo(id_conta: int):
    return 123.45

@router.post("/", status_code=status.HTTP_201_CREATED)
#@router.post("/", response_model=ContaOut, status_code=status.HTTP_201_CREATED)
async def criar_conta(conta:ContaIn):
    return "Conta criada"

@router.patch("/{id_conta}", status_code=status.HTTP_202_ACCEPTED)
#@router.patch("/{id_conta}", status_code=status.HTTP_202_ACCEPTED, response_model=ContaOut)
async def editar_conta(id_conta:int, conta:ContaInEdit):
    return "Conta editada como sucesso!"

@router.delete("/{id_conta}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_conta(id_conta: int):
    return
