"""create document table

Revision ID: bd28c3f32fec
Revises: 
Create Date: 2016-09-15 21:06:10.812965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd28c3f32fec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'documents',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(250)),
        sa.Column('path', sa.String(1000))
    )


def downgrade():
    op.drop_table('documents')
