"""create relationship tables

Revision ID: 74d5d1b09e47
Revises: b3ed56bdf12d
Create Date: 2016-09-15 21:15:46.336740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74d5d1b09e47'
down_revision = 'b3ed56bdf12d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'author_documents',
        sa.Column('author_id', sa.Integer, sa.ForeignKey('authors.id'), primary_key=True),
        sa.Column('document_id', sa.Integer, sa.ForeignKey('documents.id'), primary_key=True)
    )

    op.create_table(
        'document_categories',
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'), primary_key=True),
        sa.Column('document_id', sa.Integer, sa.ForeignKey('documents.id'), primary_key=True)
    )

    op.create_table(
        'document_publishers',
        sa.Column('publisher_id', sa.Integer, sa.ForeignKey('publishers.id'), primary_key=True),
        sa.Column('document_id', sa.Integer, sa.ForeignKey('documents.id'), primary_key=True)
    )

    op.create_table(
        'document_journals',
        sa.Column('journal_id', sa.Integer, sa.ForeignKey('journals.id'), primary_key=True),
        sa.Column('document_id', sa.Integer, sa.ForeignKey('documents.id'), primary_key=True)
    )


def downgrade():
    op.drop_table('author_documents')
    op.drop_table('document_categories')
    op.drop_table('document_publishers')
    op.drop_table('document_journals')