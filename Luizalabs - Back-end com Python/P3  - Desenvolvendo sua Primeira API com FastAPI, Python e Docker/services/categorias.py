from database.connection import engine
from database.connection import Categorias
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import text


### CORE #########################


def core_get_all():
    stmt = text("SELECT * FROM categorias")
    with engine.connect() as conn:
        results = conn.execute(stmt).mappings().all()
        return [dict(row) for row in results]

def core_post(json_data):
    with engine.connect() as conn:
        stmt = text("INSERT INTO categorias (nome) VALUES (:nome)")
        conn.execute(stmt, {"nome": json_data.nome})
        conn.commit()

def core_get(id):
    stmt = text("SELECT * FROM categorias WHERE id=:id").bindparams(id=id)
    with engine.connect() as conn:
        results = conn.execute(stmt)
        return [result for result in results.mappings()]    

### ORM  #########################



def orm_get_all():
    stmt = select(Categorias)
    # with Session(engine) as session:
    with engine.connect() as conn:
        results = conn.execute(stmt).mappings().all()
        return results

def orm_post(json_data):
    with Session(engine) as session:
        nova_categoria = Categorias(
            nome=json_data.nome
        )
        session.add(nova_categoria)
        session.commit()

def orm_get(id):
    stmt = select(Categorias).where(Categorias.id == id)
    with Session(engine) as session:
        results = session.execute(stmt).scalars().all()
        return results