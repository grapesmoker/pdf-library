"""create additional models

Revision ID: b3ed56bdf12d
Revises: bd28c3f32fec
Create Date: 2016-09-15 21:11:01.956394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3ed56bdf12d'
down_revision = 'bd28c3f32fec'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'authors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(250)),
        sa.Column('last_name', sa.String(250)),
        sa.Column('middle_name', sa.String(250)),
    )

    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(250)),
    )

    op.create_table(
        'publishers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(250)),
    )


def downgrade():
    op.drop_table('authors')
    op.drop_table('categories')
    op.drop_table('publishers')
