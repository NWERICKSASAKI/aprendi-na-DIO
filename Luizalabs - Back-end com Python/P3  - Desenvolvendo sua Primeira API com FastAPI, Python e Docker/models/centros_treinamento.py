
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Column

# Método CORE

def get_core_centros_treinamento_table(metadata):
    return Table(
        "centros_treinamento",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nome", String(20)),
        Column("endereco", String(60)),
        Column("proprietario", String(30))
    )

# Método ORM

def get_orm_centros_treinamento_table(base):

    class CentrosTreinamento(base):
        __tablename__ = "centros_treinamento"
        id = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(20))
        endereco = Column(String(60)),
        proprietario = Column(String(30))

        def __repr__(self):
            return f"CentrosTreinamento(id={self.id}, nome={self.nome}, endereco={self.endereco}, proprietario={self.proprietario})"

    return CentrosTreinamento
