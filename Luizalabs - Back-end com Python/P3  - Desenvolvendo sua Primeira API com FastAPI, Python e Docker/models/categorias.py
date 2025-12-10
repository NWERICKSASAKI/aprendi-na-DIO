from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Column

# Método CORE

def get_core_categorias_table(metadata):
    return Table(
        "categorias",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nome", String(10), unique=True, nullable=False),
    )

# Método ORM

def get_orm_categorias_table(base):

    class Categorias(base):
        __tablename__ = "categorias"
        id = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(10), unique=True, nullable=False)

        def __repr__(self):
            return f"Categorias(id={self.id}, nome={self.nome})"

    return Categorias
