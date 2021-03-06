"""empty message

Revision ID: 7e2bd7ee31b7
Revises: 
Create Date: 2020-07-03 03:52:08.142462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e2bd7ee31b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('smtpemail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('host', sa.String(), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('smtpemail')
    # ### end Alembic commands ###
