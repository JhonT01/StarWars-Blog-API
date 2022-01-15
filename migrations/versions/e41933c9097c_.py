"""empty message

Revision ID: e41933c9097c
Revises: f39d443e1cad
Create Date: 2022-01-15 00:48:58.805502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e41933c9097c'
down_revision = 'f39d443e1cad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('skin_color', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('homeworld', sa.String(length=250), nullable=True),
    sa.Column('films', sa.String(length=250), nullable=True),
    sa.Column('species', sa.String(length=250), nullable=True),
    sa.Column('vehicles', sa.String(length=250), nullable=True),
    sa.Column('starships', sa.String(length=250), nullable=True),
    sa.Column('created', sa.String(length=250), nullable=True),
    sa.Column('edited', sa.String(length=250), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(length=250), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.Column('surface_water', sa.Integer(), nullable=True),
    sa.Column('created', sa.String(length=250), nullable=True),
    sa.Column('edited', sa.String(length=250), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=True),
    sa.Column('vehicle_class', sa.String(length=250), nullable=True),
    sa.Column('manufacturer', sa.String(length=250), nullable=True),
    sa.Column('cost_in_credits', sa.Integer(), nullable=True),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('max_atmosphering_speed', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.Integer(), nullable=True),
    sa.Column('consumables', sa.String(length=250), nullable=True),
    sa.Column('films', sa.String(length=250), nullable=True),
    sa.Column('pilots', sa.String(length=250), nullable=True),
    sa.Column('created', sa.String(length=250), nullable=True),
    sa.Column('edited', sa.String(length=250), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite__people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite__planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite__vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite__vehicle')
    op.drop_table('favorite__planet')
    op.drop_table('favorite__people')
    op.drop_table('vehicle')
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###
