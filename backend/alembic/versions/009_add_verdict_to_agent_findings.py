"""Add verdict column to agent_findings

Revision ID: 009_add_verdict_to_agent_findings
Revises: 008_add_files_with_findings
Create Date: 2026-05-04

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '009_add_verdict_to_agent_findings'
down_revision = '008_add_files_with_findings'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('agent_findings', sa.Column('verdict', sa.String(length=30), nullable=True))


def downgrade() -> None:
    op.drop_column('agent_findings', 'verdict')
