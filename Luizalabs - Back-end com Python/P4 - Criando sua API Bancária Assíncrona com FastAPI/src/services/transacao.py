import sqlalchemy as sa
from src.database import database
from src.models.conta import conta, conta_corrente, conta_empresarial
from src.models.transacao import transacao
from datetime import datetime, timezone


async def listar_transacoes():
    pass


async def visualizar_transacao(transacao_id: int):
    pass


async def visualizar_extrato_cliente(cliente_id: int):
    pass


async def realizar_saque(transacao_json):
    pass


async def realizar_deposito(transacao_json):
    pass