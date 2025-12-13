from database.connection import engine
from database.connection import Atletas
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import text


### CORE #########################

# POST /atletas/
def core_post(json_data):
    with engine.connect() as conn:
        stmt = text("INSERT INTO atletas (nome, cpf, idade, peso, altura, sexo, centro_treinamento_id, categoria_id) VALUES (:nome, :cpf, :idade, :peso, :altura, :sexo, :centro_treinamento_id, :categoria_id)")
        conn.execute(stmt, {
            "nome": json_data.nome,
            "cpf": json_data.cpf,
            "idade": json_data.idade,
            "peso": json_data.peso,
            "altura": json_data.altura,
            "sexo": json_data.sexo,
            "centro_treinamento_id": json_data.centro_treinamento_id,
            "categoria_id": json_data.categoria_id,
            })
        conn.commit()

# GET /atletas/
def core_get_all():
    stmt = text("SELECT * FROM atletas")
    with engine.connect() as conn:
        results = conn.execute(stmt).mappings().all()
        return [dict(row) for row in results]

# GET /atletas/{id}
def core_get(id):
    stmt = text("SELECT * FROM atletas WHERE id=:id").bindparams(id=id)
    with engine.connect() as conn:
        results = conn.execute(stmt)
        return [result for result in results.mappings()]    

# PATCH /atletas/{id}


# DELETE /atletas/{id}
def core_delete(id):
    stmt = text("DELETE FROM atletas WHERE id=:id").bindparams(id=id)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

### ORM  #########################


# POST /atletas/
def orm_post(json_data):
    with Session(engine) as session:
        nova_categoria = Atletas(
            nome = json_data.nome,
            cpf = json_data.cpf,
            idade = json_data.idade,
            peso = json_data.peso,
            altura = json_data.altura,
            sexo = json_data.sexo,
            centro_treinamento_id = json_data.centro_treinamento_id,
            categoria_id = json_data.categoria_id,
        )
        session.add(nova_categoria)
        session.commit()

# GET /atletas/
def orm_get_all():
    stmt = select(Atletas)
    # with Session(engine) as session:
    with engine.connect() as conn:
        results = conn.execute(stmt).mappings().all()
        return results

# GET /atletas/{id}  
def orm_get(id):
    stmt = select(Atletas).where(Atletas.id == id)
    with Session(engine) as session:
        results = session.execute(stmt).scalars().all()
        return results

# PATCH /atletas/{id}


# DELETE /atletas/{id}
def orm_delete(id):
    stmt = select(Atletas).where(Atletas.id == id)
    with Session(engine) as session:
        atleta_deletar = session.execute(stmt).scalars().first()
        session.delete(atleta_deletar)
        session.commit()

