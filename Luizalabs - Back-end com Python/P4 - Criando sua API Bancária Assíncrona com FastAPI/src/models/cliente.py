import sqlalchemy as sa
from src.database import metadata

cliente = sa.Table(
    'cliente',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('senha', sa.String),
    sa.Column('endereco', sa.String),
    sa.Column('cadastrado_em', sa.TIMESTAMP(timezone=True), nullable=True)
    )

pessoa_fisica = sa.Table(
    'pessoa_fisica',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('cliente_id', sa.Integer, sa.ForeignKey('cliente.id', ondelete='CASCADE')),
    sa.Column('cpf', sa.String(14), nullable=False, unique=True),
    sa.Column('nome', sa.String(150), nullable=False),
    sa.Column('nascimento', sa.Date, nullable=True),
    )

pessoa_juridica = sa.Table(
    'pessoa_juridica',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('cliente_id', sa.Integer, sa.ForeignKey('cliente.id', ondelete='CASCADE')),
    sa.Column('cnpj', sa.String(), nullable=False, unique=True),
    sa.Column('razao_social', sa.String(150), nullable=False)
)
