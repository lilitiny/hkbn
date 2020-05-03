"""Pay_Table

Revision ID: 92e71c42e9f5
Revises: 57fe3a73c0cb
Create Date: 2020-05-02 20:57:14.659494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92e71c42e9f5'
down_revision = '57fe3a73c0cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pay',
    sa.Column('Payid', sa.Integer(), nullable=False),
    sa.Column('planid', sa.Integer(), nullable=True),
    sa.Column('Paydate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('Payid')
    )
    op.create_index(op.f('ix_pay_Paydate'), 'pay', ['Paydate'], unique=False)
    op.create_index(op.f('ix_pay_planid'), 'pay', ['planid'], unique=False)
    op.drop_table('e_service')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('e_service',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('SerName', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index(op.f('ix_pay_planid'), table_name='pay')
    op.drop_index(op.f('ix_pay_Paydate'), table_name='pay')
    op.drop_table('pay')
    # ### end Alembic commands ###