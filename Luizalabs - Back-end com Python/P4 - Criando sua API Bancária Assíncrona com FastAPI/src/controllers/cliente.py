from fastapi import APIRouter, Depends, status

from src.schemas.cliente import PessoaFisicaIn, PessoaJuridicaIn
from src.schemas.transacao import TransacaoIn
from src.views.cliente import PessoaFisicaOut, PessoaJuridicaOut 
from src.views.transacao import TransacaoOut
from src.services import cliente as services


from typing import Union

ClienteIn = Union[PessoaFisicaIn, PessoaJuridicaIn]
ClienteOut = Union[PessoaFisicaOut, PessoaJuridicaOut]

# TODO adicionar dependencias de login com Depends

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
#@router.get("/", response_model=list[ClienteOut])
async def listar_clientes():
    return await services.listar_clientes()

@router.get("/{cliente_id}")
#@router.get("/{cliente_id}", response_model=ClienteOut)
async def obter_cliente(cliente_id: int):
    return await services.resgatar_cliente(cliente_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
#@router.post("/", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente_json: ClienteIn):
    cliente_id = await services.criar_cliente(cliente_json)
    return {"id": cliente_id}

@router.patch("/{cliente_id}", status_code=status.HTTP_202_ACCEPTED)
#@router.patch("/{cliente_id}", response_model=ClienteOut, status_code=status.HTTP_202_ACCEPTED)
async def atualizar_cliente(cliente_id: int, cliente: ClienteIn):
    return f"Cliente {cliente_id} atualizado com sucesso: {cliente}"

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(cliente_id: int):
    return

