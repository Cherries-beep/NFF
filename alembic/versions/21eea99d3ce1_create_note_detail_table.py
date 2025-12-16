from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = '0002_create_note_detail_table'
down_revision = '0001_create_notes_table'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'note_detail',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('note_id', sa.Integer, sa.ForeignKey('notes.id'), unique=True),
        sa.Column('extra_info', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
    )

def downgrade():
    op.drop_table('note_detail')
