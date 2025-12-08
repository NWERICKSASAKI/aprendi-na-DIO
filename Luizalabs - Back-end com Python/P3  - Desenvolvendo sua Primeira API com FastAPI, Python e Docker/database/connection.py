from sqlalchemy import create_engine
from sqlalchemy import MetaData
from models.atletas import get_core_atletas_table, get_orm_atletas_table
from models.categorias import get_core_categorias_table, get_orm_categorias_table
from models.centros_treinamento import get_core_centros_treinamento_table, get_orm_centros_treinamento_table
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///database/workout.db', echo=True)

def create_core_db():
    metadata = MetaData()
    get_core_centros_treinamento_table(metadata)
    get_core_atletas_table(metadata)
    get_core_categorias_table(metadata)
    metadata.create_all(engine)

def create_orm_db():
    Base = declarative_base()
    get_orm_centros_treinamento_table(Base)
    get_orm_atletas_table(Base)
    get_orm_categorias_table(Base)
    Base.metadata.create_all(engine)