import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.database import metadata
from database import Base, metadata

# CORE

clientes = sa.Table(
    'clientes',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('cpf', sa.String(14), nullable=False, unique=True),
    sa.Column('nome', sa.String(150), nullable=False),
    sa.Column('nascimento', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('cadastrado_em', sa.TIMESTAMP(timezone=True), nullable=True),
    )

# ORM

