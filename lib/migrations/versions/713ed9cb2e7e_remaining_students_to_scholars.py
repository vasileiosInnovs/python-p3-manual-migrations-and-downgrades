"""Remaining students to scholars

Revision ID: 713ed9cb2e7e
Revises: 791279dd0760
Create Date: 2025-05-22 21:03:11.139829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '713ed9cb2e7e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
