from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Column

def get_atletas_table(metadata):
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
        Column("centro_treinamento_id", Integer),
        Column("categoria_id", Integer)
    )