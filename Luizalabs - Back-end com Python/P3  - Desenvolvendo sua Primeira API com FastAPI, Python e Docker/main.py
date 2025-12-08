from fastapi import FastAPI
from controllers import atletas
from controllers import categorias
from controllers import centros_treinamento

app = FastAPI()
app.include_router(atletas.router)
app.include_router(categorias.router)
app.include_router(centros_treinamento.router)