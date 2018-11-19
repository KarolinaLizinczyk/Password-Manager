"""empty message

Revision ID: f28df0443141
Revises: 376840873f89
Create Date: 2018-11-19 20:02:24.734000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f28df0443141'
down_revision = '376840873f89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('password_manager', sa.Column('_password', sa.Binary(), nullable=True))
    op.drop_column('password_manager', 'login_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('password_manager', sa.Column('login_password', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.drop_column('password_manager', '_password')
    # ### end Alembic commands ###
