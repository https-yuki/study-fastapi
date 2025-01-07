from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

# Define the ENUM type without recreating it
item_status_enum = ENUM('ON_SALE', 'SOLD_OUT', name='itemstatus', create_type=False)

revision = '5313aa3b4d23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Ensure ENUM type exists before creating the table
    op.execute("""
    DO $$ 
    BEGIN 
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'itemstatus') THEN
            CREATE TYPE itemstatus AS ENUM ('ON_SALE', 'SOLD_OUT');
        END IF;
    END $$;
    """)
    
    # Create the table
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('status', item_status_enum, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_id'), 'items', ['id'], unique=False)


def downgrade():
    # Drop the table
    op.drop_index(op.f('ix_items_id'), table_name='items')
    op.drop_table('items')

    # Drop ENUM type
    op.execute("DROP TYPE IF EXISTS itemstatus")
