import sqlalchemy as sa
from src.database import metadata

conta = sa.Table(
    'conta',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('saldo', sa.Float),
    sa.Column('numero', sa.Integer, unique=True, autoincrement=True),
    sa.Column('agencia', sa.String(4)),
    sa.Column('cliente_id', sa.Integer, sa.ForeignKey('cliente.id')),
    sa.Column('historico_id', sa.Integer, sa.ForeignKey('transacao.id')),
    sa.Column('cadastrado_em', sa.TIMESTAMP(timezone=True), nullable=True)
)

conta_corrente = sa.Table(
    'conta_corrente',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('tipo', sa.String(1)),
    sa.Column('conta_id', sa.Integer, sa.ForeignKey('conta.id', ondelete='CASCADE')),
    sa.Column('limite', sa.Float),
    sa.Column('limite_saque', sa.Integer)
)

conta_empresarial = sa.Table(
    'conta_empresarial',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('tipo', sa.String(1)),
    sa.Column('conta_id', sa.Integer, sa.ForeignKey('conta.id', ondelete='CASCADE')),
    sa.Column('emprestimo', sa.Float),
    sa.Column('emprestimo_limite', sa.Float)
)