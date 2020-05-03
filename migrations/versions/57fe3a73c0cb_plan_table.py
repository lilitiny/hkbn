"""Plan_Table

Revision ID: 57fe3a73c0cb
Revises: c614a59acde6
Create Date: 2020-05-01 20:11:43.720337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57fe3a73c0cb'
down_revision = 'c614a59acde6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('e_service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('SerName', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Pname', sa.String(length=20), nullable=True),
    sa.Column('Price', sa.Integer(), nullable=True),
    sa.Column('Speed', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plan')
    op.drop_table('e_service')
    # ### end Alembic commands ###