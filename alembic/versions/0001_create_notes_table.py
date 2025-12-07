"""create notes table

Revision ID: 0001_create_notes_table
Revises:
Create Date: 2025-12-06 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_create_notes_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'notes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('content', sa.Text, nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
    )

def downgrade():
    op.drop_table('notes')