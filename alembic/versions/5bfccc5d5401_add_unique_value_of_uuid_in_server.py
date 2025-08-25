"""ADD unique value of UUID in server

Revision ID: 5bfccc5d5401
Revises: 420ffb50e46c
Create Date: 2025-08-23 18:05:13.059848

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as pg


# revision identifiers, used by Alembic.
revision: str = '5bfccc5d5401'
down_revision: Union[str, Sequence[str], None] = '420ffb50e46c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Make sure the function exists (safe if already there)
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")

    # Backfill (no rows yet? still safe)
    op.execute("UPDATE country       SET country_uuid        = gen_random_uuid() WHERE country_uuid IS NULL;")
    op.execute("UPDATE stateorregion SET state_or_region_uuid= gen_random_uuid() WHERE state_or_region_uuid IS NULL;")
    op.execute("UPDATE province      SET province_uuid       = gen_random_uuid() WHERE province_uuid IS NULL;")
    op.execute("UPDATE city          SET city_uuid           = gen_random_uuid() WHERE city_uuid IS NULL;")
    op.execute("UPDATE locality      SET locality_uuid       = gen_random_uuid() WHERE locality_uuid IS NULL;")

    # Add server defaults (so raw inserts omit column and still get a value)
    op.alter_column(
        "country", "country_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=sa.text("gen_random_uuid()"),
    )
    op.alter_column(
        "stateorregion", "state_or_region_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=sa.text("gen_random_uuid()"),
    )
    op.alter_column(
        "province", "province_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=sa.text("gen_random_uuid()"),
    )
    op.alter_column(
        "city", "city_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=sa.text("gen_random_uuid()"),
    )
    op.alter_column(
        "locality", "locality_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=sa.text("gen_random_uuid()"),
    )


def downgrade():
    # Drop server defaults (keep NOT NULL as-is)
    op.alter_column(
        "locality", "locality_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=None,
    )
    op.alter_column(
        "city", "city_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=None,
    )
    op.alter_column(
        "province", "province_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=None,
    )
    op.alter_column(
        "stateorregion", "state_or_region_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=None,
    )
    op.alter_column(
        "country", "country_uuid",
        existing_type=pg.UUID(), existing_nullable=False,
        server_default=None,
    )