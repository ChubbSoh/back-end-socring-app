"""empty message

Revision ID: 3511b207b36a
Revises: 64216d73c4ee
Create Date: 2018-12-21 14:38:08.994136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3511b207b36a'
down_revision = '64216d73c4ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=False))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
