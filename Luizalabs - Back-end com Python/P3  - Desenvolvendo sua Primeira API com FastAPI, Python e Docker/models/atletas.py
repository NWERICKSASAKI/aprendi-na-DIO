from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


# Método CORE

def core_get_atletas_table(metadata):
    return Table(
        "atletas",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nome", String(50)),
        Column("cpf", String(11), unique=True),
        Column("idade", Integer),
        Column("peso", Integer),
        Column("altura", Integer),
        Column("sexo", String(1)),
        Column("centro_treinamento_id", Integer, ForeignKey("centros_treinamento.id")),
        Column("categoria_id", Integer, ForeignKey("categorias.id")),
    )

# Método ORM

def orm_get_atletas_table(base):

    class Atletas(base):
        __tablename__ = "atletas"
        id = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(50))
        cpf = Column(String(11), unique=True, nullable=False)
        idade = Column(Integer)
        peso = Column(Integer)
        altura = Column(Integer)
        sexo = Column(String(1))
        centro_treinamento_id = Column(Integer, ForeignKey("centros_treinamento.id"))
        categoria_id = Column(Integer, ForeignKey("categorias.id"))
        #centro_treinamento_id = relationship("centros_treinamento", back_populates="atletas")
        #categoria_id = relationship("categorias", back_populates="atletas")

        def __repr__(self):
            return f"""Atletas(
                        id={self.id}, 
                        nome={self.nome}, 
                        cpf={self.cpf}, 
                        idade={self.idade},
                        peso={self.peso},
                        altura={self.altura},
                        sexo={self.sexo},
                        centro_treinamento_id={self.centro_treinamento_id},
                        categoria_id={self.categoria_id},
                        )"""
    return Atletas
