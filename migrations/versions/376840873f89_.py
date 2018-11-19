"""empty message

Revision ID: 376840873f89
Revises: 
Create Date: 2018-11-19 16:55:25.501000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '376840873f89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('password_manager',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('site_name', sa.String(length=64), nullable=False),
    sa.Column('site_url', sa.String(length=128), nullable=False),
    sa.Column('login_account_name', sa.String(length=128), nullable=False),
    sa.Column('login_password', sa.Binary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('password_manager')
    # ### end Alembic commands ###