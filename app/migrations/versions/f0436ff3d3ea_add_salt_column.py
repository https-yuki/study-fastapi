"""Add salt column

Revision ID: f0436ff3d3ea
Revises: 1685f4d8eb10
Create Date: 2025-01-01 08:43:55.589442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0436ff3d3ea'
down_revision: Union[str, None] = '1685f4d8eb10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('salt', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'salt')
    # ### end Alembic commands ###