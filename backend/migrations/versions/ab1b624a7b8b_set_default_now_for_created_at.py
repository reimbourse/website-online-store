"""set default now for created_at

Revision ID: ab1b624a7b8b
Revises: c0615c53271d
Create Date: 2026-11-13 20:42:09.178154

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab1b624a7b8b'
down_revision: Union[str, Sequence[str], None] = 'c0615c53271d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )
    # Рекомендуется сразу добавить и для остальных таблиц с датами:
    op.alter_column(
        "cart_items",
        "added_at",
        existing_type=sa.DateTime(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )
    op.alter_column(
        "favorites",
        "added_at",
        existing_type=sa.DateTime(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )
    op.alter_column(
        "orders",
        "created_at",
        existing_type=sa.DateTime(),
        server_default=sa.text("now()"),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
