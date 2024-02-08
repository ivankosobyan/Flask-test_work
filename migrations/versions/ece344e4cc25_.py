"""empty message

Revision ID: ece344e4cc25
Revises: 
Create Date: 2024-02-07 14:02:47.781807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ece344e4cc25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctors', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('doctors', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('services', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('services', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('services', 'updated_at')
    op.drop_column('services', 'created_at')
    op.drop_column('doctors', 'updated_at')
    op.drop_column('doctors', 'created_at')
    # ### end Alembic commands ###
