from fastapi import APIRouter, Depends, status

from src.schemas.cliente import PessoaFisicaIn, PessoaJuridicaIn
from src.schemas.cliente import PessoaFisicaInEdit, PessoaJuridicaInEdit
from src.views.cliente import PessoaFisicaOut, PessoaJuridicaOut 
from src.services import cliente as services

from pydantic import Field
from typing import Union, Annotated

ClienteIn = Union[PessoaFisicaIn, PessoaJuridicaIn]
ClienteInEdit = Union[PessoaFisicaInEdit, PessoaJuridicaInEdit]
ClienteOut = Annotated[
    Union[PessoaFisicaOut, PessoaJuridicaOut],
    Field(discriminator="tipo")
]

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/", response_model=list[ClienteOut])
async def listar_clientes():
    return await services.listar_clientes()

@router.get("/{cliente_id}", response_model=ClienteOut)
async def obter_cliente(cliente_id: int):
    cliente = await services.obter_cliente(cliente_id)
    return cliente

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_cliente(cliente_json: ClienteIn):
    cliente_id = await services.criar_cliente(cliente_json)
    return f"Cliente id {cliente_id} criado com sucesso!"

@router.patch("/{cliente_id}", status_code=status.HTTP_202_ACCEPTED)
async def atualizar_cliente(cliente_id: int, cliente: ClienteInEdit):
    await services.atualizar_cliente(cliente_id, cliente)
    return f"Cliente id {cliente_id} editado com sucesso!"

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_cliente(cliente_id: int):
    await services.deletar_cliente(cliente_id)
    return

