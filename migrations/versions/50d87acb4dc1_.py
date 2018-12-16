"""empty message

Revision ID: 50d87acb4dc1
Revises: 8c18ebb57414
Create Date: 2018-12-16 14:49:46.131830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50d87acb4dc1'
down_revision = '8c18ebb57414'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=False))
    op.add_column('todos', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'created_at')
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
