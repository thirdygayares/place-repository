"""Add extension for UUID

Revision ID: 420ffb50e46c
Revises: f3edf03a0cb2
Create Date: 2025-08-23 17:55:09.139984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '420ffb50e46c'
down_revision: Union[str, Sequence[str], None] = 'f3edf03a0cb2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute('CREATE EXTENSION IF NOT EXISTS pgcrypto;')

def downgrade():
    op.execute('DROP EXTENSION IF EXISTS pgcrypto;')