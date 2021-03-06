"""Initial migration

Revision ID: e8ba76bdb645
Revises: 
Create Date: 2020-04-21 23:22:48.351313

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = 'e8ba76bdb645'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    if 'person' in tables:
        op.drop_table('person') #Remove this when "subscribie init" no longer
                                # is called by module_builder
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sid', sa.String(), nullable=True),
    sa.Column('ts', sa.DateTime(), nullable=True),
    sa.Column('given_name', sa.String(), nullable=True),
    sa.Column('family_name', sa.String(), nullable=True),
    sa.Column('address_line1', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('mobile', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.String(), nullable=True),
    sa.Column('login_token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('person')
    # ### end Alembic commands ###
