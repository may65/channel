"""empty message

Revision ID: 172fbb1e1953
Revises: 
Create Date: 2023-04-07 18:40:29.411737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '172fbb1e1953'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('num_ord', sa.Integer(), nullable=True),
    sa.Column('cost_s', sa.Float(), nullable=True),
    sa.Column('date', sa.String(length=32), nullable=True),
    sa.Column('cost_r', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###
