"""third Migration

Revision ID: 0a2d5218ff0d
Revises: 53eddb28f6aa
Create Date: 2020-11-01 12:25:03.030616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a2d5218ff0d'
down_revision = '53eddb28f6aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('opinion', sa.String(length=255), nullable=True))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('comments', 'opinion')
    # ### end Alembic commands ###
