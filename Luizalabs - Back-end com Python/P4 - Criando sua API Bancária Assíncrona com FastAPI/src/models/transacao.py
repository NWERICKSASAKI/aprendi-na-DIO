import sqlalchemy as sa
from src.database import metadata

transacao = sa.Table(
    'transacao',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('conta_id', sa.Integer, sa.ForeignKey('conta.id')),
    sa.Column('valor', sa.Float, nullable=False),
    sa.Column('tipo', sa.String(1), nullable=False),
    sa.Column('cadastrado_em', sa.TIMESTAMP(timezone=True), nullable=False)
)
