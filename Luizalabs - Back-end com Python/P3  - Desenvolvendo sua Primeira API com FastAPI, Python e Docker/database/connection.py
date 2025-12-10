from sqlalchemy import create_engine

engine = create_engine('sqlite:///database/workout.db', echo=True)

#############
#   CORE    

from sqlalchemy import MetaData
metadata = MetaData()

def core_load_tables():
    from models.atletas import core_get_atletas_table
    from models.categorias import core_get_categorias_table
    from models.centros_treinamento import core_get_centros_treinamento_table

    core_get_centros_treinamento_table(metadata)
    core_get_categorias_table(metadata)
    core_get_atletas_table(metadata)

def core_create_db():
    core_load_tables
    metadata.create_all(engine)


#############
#   ORM    

from sqlalchemy.orm import declarative_base
Base = declarative_base()

def orm_load_tables():
    from models.atletas import orm_get_atletas_table
    from models.categorias import orm_get_categorias_table
    from models.centros_treinamento import orm_get_centros_treinamento_table

    Centros_Treinamento = orm_get_centros_treinamento_table(Base)
    Categorias = orm_get_categorias_table(Base)
    Atletas = orm_get_atletas_table(Base)
    return Centros_Treinamento, Categorias, Atletas

def orm_create_db():
    Base.metadata.create_all(engine)

Centros_Treinamento, Categorias, Atletas = orm_load_tables()
