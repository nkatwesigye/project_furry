"""empty message

Revision ID: f9132390028b
Revises: eb02de174736
Create Date: 2020-02-04 18:50:49.943788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9132390028b'
down_revision = 'eb02de174736'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Shows', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint('Shows_name_fkey', 'Shows', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('Shows_name_fkey', 'Shows', 'Venue', ['name'], ['name'])
    op.alter_column('Shows', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###