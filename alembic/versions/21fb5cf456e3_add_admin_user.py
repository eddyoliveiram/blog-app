from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

revision = '21fb5cf456e3'
down_revision = '285b09f5367f'
branch_labels = None
depends_on = None

users_table = table(
    'users',
    column('id', Integer),
    column('username', String),
    column('email', String),
    column('hashed_password', String)
)

def upgrade():
    op.bulk_insert(users_table,
        [
            {'id': 1, 'username': 'admin', 'email': 'admin@example.com', 'hashed_password': 'admin'}
        ]
    )

def downgrade():
    op.execute("DELETE FROM users WHERE username = 'admin'")
