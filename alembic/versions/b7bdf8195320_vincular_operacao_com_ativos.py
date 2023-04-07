"""vincular operacao com ativos

Revision ID: b7bdf8195320
Revises: 1f686649c7f9
Create Date: 2023-04-06 20:38:27.765988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7bdf8195320'
down_revision = '1f686649c7f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('operacao', sa.Column('ativo_carteira_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'operacao', 'carteira', ['ativo_carteira_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'operacao', type_='foreignkey')
    op.drop_column('operacao', 'ativo_carteira_id')
    # ### end Alembic commands ###