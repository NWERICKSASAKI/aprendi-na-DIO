from fastapi import APIRouter, Depends, status

from src.schemas.conta import ContaCorrenteIn, ContaEmpresarialIn
from src.schemas.conta import ContaCorrenteInEdit, ContaEmpresarialInEdit
from src.views.conta import ContaCorrenteOut, ContaEmpresarialOut
from src.views.transacao import TransacaoOut
from src.services import conta as services

from pydantic import Field
from typing import Union, Annotated

ContaIn = Union[ContaCorrenteIn,ContaEmpresarialIn]
ContaInEdit = Union[ContaCorrenteInEdit,ContaEmpresarialInEdit]
ContaOut = Annotated[
    Union[ContaCorrenteOut,ContaEmpresarialOut],
    Field(discriminator="tipo")
]

router = APIRouter(prefix="/contas", tags=["Contas"])

@router.get("/", response_model=list[ContaOut])
async def listar_contas():
    return await services.listar_contas()

@router.get("/{conta_id}", response_model=ContaOut)
async def obter_conta(conta_id: int):
    return await services.obter_conta(conta_id)

@router.get("/{conta_id}/saldo/", response_model=float)
async def exibir_saldo(conta_id: int):
    return await services.exibir_saldo(conta_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_conta(conta:ContaIn):
    conta_id = await services.criar_conta(conta)
    return f"Criado conta ID {conta_id} com sucesso!"

@router.patch("/{conta_id}", status_code=status.HTTP_202_ACCEPTED)
async def editar_conta(conta_id:int, conta:ContaInEdit):
    await services.editar_conta(conta_id, conta)
    return f"Conta ID {conta_id} editada com sucesso!"

@router.delete("/{conta_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_conta(conta_id: int):
    await services.deletar_conta(conta_id)
    return
