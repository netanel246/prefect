"""Add retry and restart metadata

Revision ID: 8ea825da948d
Revises: ad4b1b4d1e9d
Create Date: 2022-10-19 16:51:10.239643

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8ea825da948d"
down_revision = "6d548701edef"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "flow_run",
        sa.Column("restarts", sa.Integer(), server_default="0", nullable=False),
    )
    op.add_column(
        "task_run",
        sa.Column(
            "flow_retry_attempt", sa.Integer(), server_default="0", nullable=False
        ),
    )
    op.add_column(
        "task_run",
        sa.Column(
            "flow_restart_attempt", sa.Integer(), server_default="0", nullable=False
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("task_run", "flow_restart_attempt")
    op.drop_column("task_run", "flow_retry_attempt")
    op.drop_column("flow_run", "restarts")
    # ### end Alembic commands ###
