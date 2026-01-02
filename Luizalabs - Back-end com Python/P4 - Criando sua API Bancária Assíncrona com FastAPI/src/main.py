from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.database import database
from src.controllers import cliente
from src.controllers import conta
from src.controllers import autenticacao
from src.controllers import transacao

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

# TODO adicionar middlewares e configurações do APP
app = FastAPI(
    lifespan=lifespan
)

app.include_router(autenticacao.router)
app.include_router(cliente.router)
app.include_router(conta.router)
app.include_router(transacao.router)
