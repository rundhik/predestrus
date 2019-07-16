"""empty message

Revision ID: 927a66500e46
Revises: adb1af71b5e8
Create Date: 2019-07-16 22:20:01.022644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '927a66500e46'
down_revision = 'adb1af71b5e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_login', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_login')
    # ### end Alembic commands ###