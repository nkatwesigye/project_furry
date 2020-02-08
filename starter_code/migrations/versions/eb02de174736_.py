"""empty message

Revision ID: eb02de174736
Revises: c0de0819f9f0
Create Date: 2020-02-04 18:29:57.302993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb02de174736'
down_revision = 'c0de0819f9f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Shows', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_foreign_key(None, 'Shows', 'Venue', ['name'], ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Shows', type_='foreignkey')
    op.alter_column('Shows', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###