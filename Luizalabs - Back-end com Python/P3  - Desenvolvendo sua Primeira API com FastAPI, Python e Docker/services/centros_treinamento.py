from database.connection import engine
from database.connection import Centros_Treinamento
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import text


### CORE #########################


def core_get_all():
    stmt = text("SELECT * FROM centros_treinamento")
    with engine.connect() as conn:
        results = conn.execute(stmt).mappings().all()
        return [dict(row) for row in results]

def core_post(json_data):
    with engine.connect() as conn:
        stmt = text("INSERT INTO centros_treinamento (nome, endereco, proprietario) VALUES (:nome, :endereco, :proprietario)")
        conn.execute(stmt, {"nome": json_data.nome, "endereco": json_data.endereco, "proprietario": json_data.proprietario})
        conn.commit()

def core_get(id):
    stmt = text("SELECT * FROM centros_treinamento WHERE id=:id").bindparams(id=id)
    with engine.connect() as conn:
        results = conn.execute(stmt)
        return [result for result in results.mappings()]    

### ORM  #########################



def orm_get_all():
    stmt = select(Centros_Treinamento)
    with engine.connect() as conn:
        results = conn.execute(stmt).mappings().all()
        return results

def orm_post(json_data):
    with Session(engine) as session:
        novo_item = Centros_Treinamento(
            nome=json_data.nome,
            endereco=json_data.endereco,
            proprietario=json_data.proprietario,
        )
        session.add(novo_item)
        session.commit()

def orm_get(id):
    stmt = select(Centros_Treinamento).where(Centros_Treinamento.id == id)
    with Session(engine) as session:
        results = session.execute(stmt).scalars().all()
        return results