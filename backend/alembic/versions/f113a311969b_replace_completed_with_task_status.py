"""replace completed with task status

Revision ID: f113a311969b
Revises: 15aedbdfd331
Create Date: 2026-07-21 12:35:16.810380

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f113a311969b'
down_revision: Union[str, Sequence[str], None] = '15aedbdfd331'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "tasks",
        sa.Column(
            "status",
            sa.Enum(
                "TODO",
                "IN_PROGRESS",
                "COMPLETED",
                "CANCELLED",
                name="taskstatus",
            ),
            nullable=False,
            server_default="TODO",
        ),
    )

    op.drop_column("tasks", "completed")
# ### end Alembic commands ###


def downgrade() -> None:
    op.add_column(
        "tasks",
        sa.Column(
            "completed",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )

    op.drop_column("tasks", "status")
