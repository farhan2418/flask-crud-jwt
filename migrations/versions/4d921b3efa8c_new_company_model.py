"""new company model

Revision ID: 4d921b3efa8c
Revises: 
Create Date: 2023-08-31 12:52:14.158102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d921b3efa8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('c_name', sa.String(), nullable=True),
    sa.Column('c_address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comp_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'company', ['comp_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('comp_id')

    op.drop_table('company')
    # ### end Alembic commands ###
