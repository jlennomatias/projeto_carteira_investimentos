"""Incluindo o cascade

Revision ID: 44d336d4cada
Revises: 7ccce4aafdc7
Create Date: 2023-04-07 11:43:29.945572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44d336d4cada'
down_revision = '7ccce4aafdc7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('ativos_carteira_carteira_id_fkey', 'ativos_carteira', type_='foreignkey')
    op.create_foreign_key(None, 'ativos_carteira', 'carteira', ['carteira_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('carteira_user_id_fkey', 'carteira', type_='foreignkey')
    op.create_foreign_key(None, 'carteira', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('operacao_carteira_id_fkey', 'operacao', type_='foreignkey')
    op.create_foreign_key(None, 'operacao', 'carteira', ['carteira_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'operacao', type_='foreignkey')
    op.create_foreign_key('operacao_carteira_id_fkey', 'operacao', 'carteira', ['carteira_id'], ['id'])
    op.drop_constraint(None, 'carteira', type_='foreignkey')
    op.create_foreign_key('carteira_user_id_fkey', 'carteira', 'user', ['user_id'], ['id'])
    op.drop_constraint(None, 'ativos_carteira', type_='foreignkey')
    op.create_foreign_key('ativos_carteira_carteira_id_fkey', 'ativos_carteira', 'carteira', ['carteira_id'], ['id'])
    # ### end Alembic commands ###