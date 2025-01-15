"""added test migration

Revision ID: 7997cd8298fa
Revises: a56fa0989d32
Create Date: 2025-01-15 21:01:51.432247

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '7997cd8298fb'
down_revision = '7997cd8298fa'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test_migration = CASE
                    WHEN rating >= 9 THEN TRUE
                    ELSE FALSE
                END
            """
        )
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            """
                UPDATE films
                SET test_migration = FALSE
            """
        )
    )