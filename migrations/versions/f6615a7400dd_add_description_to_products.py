"""add description to products

Revision ID: f6615a7400dd
Revises: c26dae3da465
Create Date: 2018-11-29 11:22:45.326229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6615a7400dd'
down_revision = 'c26dae3da465'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'description')
    # ### end Alembic commands ###
