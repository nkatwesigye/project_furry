"""empty message

Revision ID: dbb917b7d706
Revises: ce09c6835340
Create Date: 2020-01-26 14:52:00.753143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbb917b7d706'
down_revision = 'ce09c6835340'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('basket_a')
    op.drop_table('basket_b')
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    op.create_table('basket_b',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fruit', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='basket_b_pkey')
    )
    op.create_table('basket_a',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fruit', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='basket_a_pkey')
    )
    # ### end Alembic commands ###
