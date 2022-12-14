"""alter component table 0001

Revision ID: bc3d6eeeb685
Revises: fb4c568ac57b
Create Date: 2022-09-11 07:38:05.889440

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bc3d6eeeb685'
down_revision = 'fb4c568ac57b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('component', 'page_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('component', 'page_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###
