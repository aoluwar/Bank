"""Initial migration

Revision ID: xxxx
Revises: 
Create Date: 2025-11-04

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('customers',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('phone', sa.String, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )
    op.create_table('accounts',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('owner_id', sa.UUID, sa.ForeignKey('customers.id')),
        sa.Column('balance', sa.Float),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )
    op.create_table('transactions',
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('account_id', sa.UUID, sa.ForeignKey('accounts.id')),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('type', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )

def downgrade():
    op.drop_table('transactions')
    op.drop_table('accounts')
    op.drop_table('customers')