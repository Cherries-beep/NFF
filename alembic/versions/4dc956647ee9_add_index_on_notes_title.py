from alembic import op
import sqlalchemy as sa
from sqlalchemy import column

# revision identifiers
revision = '4dc956647ee9'
down_revision = '54ab043ce824'
branch_labels = None
depends_on = None

def upgrade():
    op.create_index(
        index_name='index_notes_title',
        table_name='notes',
        columns=['title'],
        unique=False
    )

def downgrade():
    op.drop_index(
        index_name='index_notes_title',
        table_name='notes'
    )