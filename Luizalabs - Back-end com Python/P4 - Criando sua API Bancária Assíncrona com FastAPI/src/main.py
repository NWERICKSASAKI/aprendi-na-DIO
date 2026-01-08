from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.database import database
from src.controllers import cliente
from src.controllers import conta
from src.controllers import autenticacao
from src.controllers import transacao
from src import exceptions

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


@app.exception_handler(exceptions.Error_401_UNAUTHORIZED)
async def unathorized(request: Request, exc: exceptions.Error_401_UNAUTHORIZED):
    return JSONResponse(
        status_code = exc.status_code,
        content={"detail": exc.message}
    )

@app.exception_handler(exceptions.Error_401_UNAUTHORIZED)
async def unathorized(request: Request, exc: exceptions.Error_401_UNAUTHORIZED):
    return JSONResponse(
        status_code = exc.status_code,
        content={"detail": exc.message}
    )

@app.exception_handler(exceptions.Error_403_FORBIDDEN)
async def unathorized(request: Request, exc: exceptions.Error_403_FORBIDDEN):
    return JSONResponse(
        status_code = exc.status_code,
        content={"detail": exc.message}
    )

@app.exception_handler(exceptions.Error_404_NOT_FOUND)
async def unathorized(request: Request, exc: exceptions.Error_404_NOT_FOUND):
    return JSONResponse(
        status_code = exc.status_code,
        content={"detail": exc.message}
    )

