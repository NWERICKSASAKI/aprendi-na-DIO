import sqlalchemy as sa
from src.database import metadata

cliente = sa.Table(
    'autenticacao',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('cliente_id', sa.Integer, sa.ForeignKey('cliente.id', ondelete='CASCADE')),
    sa.Column('senha', sa.String)
    )
