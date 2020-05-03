"""Location_Table

Revision ID: c614a59acde6
Revises: 1f778f3681f9
Create Date: 2020-05-01 16:36:08.028657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c614a59acde6'
down_revision = '1f778f3681f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('Street', sa.String(length=100), nullable=False),
    sa.Column('support', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('Street')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location')
    # ### end Alembic commands ###
