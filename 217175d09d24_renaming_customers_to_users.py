"""Renaming customers to users

Revision ID: 217175d09d24
Revises: 555e10730064
Create Date: 2023-11-08 23:15:51.814707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '217175d09d24'
down_revision = '555e10730064'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('customers', 'users')


def downgrade():
    op.rename_table('users', 'customers')
