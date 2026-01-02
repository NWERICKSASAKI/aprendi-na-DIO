import sqlalchemy as sa
from src.database import metadata
from database import Base, metadata

# CORE

cliente = sa.Table(
    'cliente',
    metadata,
    sa.Column('cliente_id', sa.Integer, primary_key=True),
    sa.Column('cpf', sa.String(14), nullable=False, unique=True),
    sa.Column('nome', sa.String(150), nullable=False),
    sa.Column('nascimento', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('cadastrado_em', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('contas', sa.ForeignKey('contas.cliente_id')),
    )
        return f"Cliente(cliente_id={self.cliente_id}, cpf={self.cpf}, nome={self.nome}, nascimento={self.nascimento}, cadastrado_em={self.cadastrado_em})"