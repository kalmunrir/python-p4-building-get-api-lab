"""added columns to bakeries and baked_goods

Revision ID: ff7dd2017edd
Revises: 308c897846ed
Create Date: 2023-10-05 10:50:54.691930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff7dd2017edd'
down_revision = '308c897846ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bakery_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_baked_goods_bakery_id_bakeries'), 'bakeries', ['bakery_id'], ['id'])

    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_baked_goods_bakery_id_bakeries'), type_='foreignkey')
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('bakery_id')

    # ### end Alembic commands ###
