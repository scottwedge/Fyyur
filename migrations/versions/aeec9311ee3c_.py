"""empty message

Revision ID: aeec9311ee3c
Revises: bb929c46a7ad
Create Date: 2020-05-16 23:10:54.760299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aeec9311ee3c'
down_revision = 'bb929c46a7ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'past_shows_count')
    op.drop_column('artists', 'upcoming_shows_count')
    op.drop_column('venues', 'past_shows_count')
    op.drop_column('venues', 'upcoming_shows_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('upcoming_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('venues', sa.Column('past_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('artists', sa.Column('upcoming_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('artists', sa.Column('past_shows_count', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
