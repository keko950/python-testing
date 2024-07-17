"""create contracts table

Revision ID: 84a945e9095b
Revises:
Create Date: 2024-07-16 17:30:59.200906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84a945e9095b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.create_table(
       "contract",
       sa.Column("id", sa.Integer, primary_key=True),
       sa.Column("name", sa.String, nullable=False),
       sa.Column("owner", sa.String, nullable=False),
       sa.Column("date", sa.DateTime),
       sa.Column("price", sa.DECIMAL)
   )


def downgrade() -> None:
   op.drop_table(
       "contract"
   )
