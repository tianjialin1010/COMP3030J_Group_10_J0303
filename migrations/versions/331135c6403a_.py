"""empty message

Revision ID: 331135c6403a
Revises: 
Create Date: 2024-04-12 06:39:42.384034

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '331135c6403a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sustainabilitydata')
    op.drop_table('warehouses')
    op.drop_table('vehicles')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_index('username')

    op.drop_table('users')
    op.drop_table('orders')
    op.drop_table('drivers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drivers',
    sa.Column('driver_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('total_mileage', mysql.DECIMAL(precision=10, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('total_emission', mysql.DECIMAL(precision=10, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('orders_count', mysql.INTEGER(), server_default=sa.text("'0'"), autoincrement=False, nullable=False),
    sa.Column('status', mysql.ENUM('available', 'unavailable'), nullable=False),
    sa.PrimaryKeyConstraint('driver_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('orders',
    sa.Column('order_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('initiator_user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('assigned_driver_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', mysql.ENUM('created', 'accepted', 'in_progress', 'completed', 'canceled'), nullable=False),
    sa.Column('destination', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('mileage', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('completed_at', mysql.TIMESTAMP(), nullable=True),
    sa.Column('vehicle_type', mysql.ENUM('large', 'small'), nullable=False),
    sa.Column('carbon_emission', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('driver_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('vehicle_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['assigned_driver_id'], ['users.user_id'], name='orders_ibfk_2'),
    sa.ForeignKeyConstraint(['driver_id'], ['drivers.driver_id'], name='fk_driver'),
    sa.ForeignKeyConstraint(['initiator_user_id'], ['users.user_id'], name='orders_ibfk_1'),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.vehicle_id'], name='fk_vehicle'),
    sa.PrimaryKeyConstraint('order_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('users',
    sa.Column('user_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('role', mysql.ENUM('driver', 'warehouse', 'admin'), nullable=False),
    sa.Column('avatar_url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('username', ['username'], unique=True)
        batch_op.create_index('email', ['email'], unique=True)

    op.create_table('vehicles',
    sa.Column('vehicle_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type', mysql.ENUM('large', 'small'), nullable=False),
    sa.Column('load_capacity', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('emission_rate', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('vehicle_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('warehouses',
    sa.Column('warehouse_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('longitude', mysql.DECIMAL(precision=9, scale=6), nullable=False),
    sa.Column('latitude', mysql.DECIMAL(precision=9, scale=6), nullable=False),
    sa.Column('city', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('capacity', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('warehouse_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('sustainabilitydata',
    sa.Column('data_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('carbon_emission', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('fuel_consumption', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('efficiency_score', mysql.DECIMAL(precision=5, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.order_id'], name='sustainabilitydata_ibfk_1'),
    sa.PrimaryKeyConstraint('data_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
