"""empty message

Revision ID: 492046b93cc5
Revises: e022e4ee6eed
Create Date: 2020-01-25 22:36:19.498174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '492046b93cc5'
down_revision = 'e022e4ee6eed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'website')
    # ### end Alembic commands ###