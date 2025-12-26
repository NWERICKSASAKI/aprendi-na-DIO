from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.database import database

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(
    lifespan=lifespan
)

#app.include_router(database.router)

#app.include_router(atletas.core_router)
#app.include_router(categorias.core_router)
#app.include_router(centros_treinamento.core_router)
#app.include_router(database.core_router)

#app.include_router(atletas.orm_router)
#app.include_router(categorias.orm_router)
#app.include_router(centros_treinamento.orm_router)
#app.include_router(database.orm_router)
