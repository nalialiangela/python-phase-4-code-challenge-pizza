"""initial migration

Revision ID: 57b9173bf11b
Revises: 04ebacf5db60
Create Date: 2024-06-28 14:43:39.522224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57b9173bf11b'
down_revision = '04ebacf5db60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
