"""empty message

Revision ID: 8dc5999a5c74
Revises: 770a2aa760e8
Create Date: 2020-02-01 18:27:52.347695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dc5999a5c74'
down_revision = '770a2aa760e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'size')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('size', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
