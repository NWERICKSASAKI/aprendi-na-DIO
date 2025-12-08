from fastapi import FastAPI
from controllers import atletas
from controllers import categorias
from controllers import centros_treinamento
from controllers import teste

app = FastAPI()
app.include_router(atletas.router)
app.include_router(categorias.router)
app.include_router(centros_treinamento.router)
app.include_router(teste.router)
