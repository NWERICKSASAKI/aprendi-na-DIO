from fastapi import APIRouter, Depends, status

from src.schemas.cliente import ClienteIn
from src.schemas.transacao import TransacaoIn
from src.views.cliente import ClienteOut
from src.views.transacao import TransacaoOut

# TODO adicionar dependencias de login com Depends

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
#@router.get("/", response_model=list[ClienteOut])
async def listar_clientes():
    return "Lista de clientes"  # TODO implementar lógica de listagem de clientes

@router.get("/{cliente_id}")
#@router.get("/{cliente_id}", response_model=ClienteOut)
async def obter_cliente(cliente_id: int):
    return f"Detalhes do cliente {cliente_id}"

@router.post("/", status_code=status.HTTP_201_CREATED)
#@router.post("/", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente: ClienteIn):
    return f"Cliente criado com sucesso: {cliente}"

@router.patch("/{cliente_id}", status_code=status.HTTP_202_ACCEPTED)
#@router.patch("/{cliente_id}", response_model=ClienteOut, status_code=status.HTTP_202_ACCEPTED)
async def atualizar_cliente(cliente_id: int, cliente: ClienteIn):
    return f"Cliente {cliente_id} atualizado com sucesso: {cliente}"

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(cliente_id: int):
    return

