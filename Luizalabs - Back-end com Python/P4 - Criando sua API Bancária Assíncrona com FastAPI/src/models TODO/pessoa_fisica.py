import sqlalchemy as sa
from sqlalchemy.orm import relationship
from src.database import metadata
from database import Base, metadata

# CORE

pessoa_fisica = sa.Table(
    'pessoa_fisica',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('cliente_id', sa.Integer, sa.ForeignKey('cliente.cliente_id')),
    sa.Column('cpf', sa.String(14), nullable=False, unique=True),
    sa.Column('nome', sa.String(150), nullable=False),
    sa.Column('nascimento', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('cadastrado_em', sa.TIMESTAMP(timezone=True), nullable=True),
)

# ORM

class PessoaFisica(Base):
    __tablename__ = "pessoa_fisica"
    id = sa.Column(sa.Integer, primary_key=True),
    cliente_id = sa.Column(sa.Integer, sa.ForeignKey('cliente.cliente_id')),
    cpf = sa.Column(sa.String(14), nullable=False, unique=True),
    nome = sa.Column(sa.String(150), nullable=False),
    nascimento = sa.Column(sa.TIMESTAMP(timezone=True), nullable=True),
    cadastrado_em = sa.Column(sa.TIMESTAMP(timezone=True), nullable=True),

    relationship("Clientes", back_populates="pessoa_fisica")

    def __repr__(self):
        return f"PessoaFisica(id={self.id}, cliente_id={self.cliente_id}, cpf={self.cpf}, nome={self.nome}, nascimento={self.nascimento}, cadastrado_em={self.cadastrado_em})"
