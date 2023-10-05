"""added price column to baked_goods

Revision ID: 308c897846ed
Revises: 1534348a80fc
Create Date: 2023-10-05 10:45:50.264111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '308c897846ed'
down_revision = '1534348a80fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.drop_column('price')

    # ### end Alembic commands ###
