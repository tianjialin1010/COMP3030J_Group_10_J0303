from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from backend.App.exts import db
from sqlalchemy import Enum
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum
from flask_sqlalchemy import SQLAlchemy


class OrderStatus(Enum):
    CREATED = 'created'
    ACCEPTED = 'accepted'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELED = 'canceled'


class Driver(db.Model):
    __tablename__ = 'drivers'
    driver_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    total_mileage = db.Column(db.Numeric(10, 2), nullable=False, default='0.00')
    total_emission = db.Column(db.Numeric(10, 2), nullable=False, default='0.00')
    orders_count = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.String(255), nullable=False)  # Simplified enum representation


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, ForeignKey('vehicles.id'))
    initiator_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    assigned_driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'))
    status = db.Column(SQLEnum(OrderStatus), nullable=False, default=OrderStatus.CREATED)
    destination = db.Column(db.String(255), nullable=False)
    startlocation = db.Column(db.String(255), nullable=False)
    mileage = db.Column(db.Numeric(10, 2), default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    vehicle_type = db.Column(db.String(255), nullable=False)  # Simplified enum representation
    carbon_emission = db.Column(db.Numeric(10, 2), default=0)
    driver = db.relationship('Driver', foreign_keys=[assigned_driver_id])


class SustainabilityData(db.Model):
    __tablename__ = 'sustainabilitydata'
    data_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    carbon_emission = db.Column(db.Numeric(10, 2), nullable=False)
    fuel_consumption = db.Column(db.Numeric(10, 2), nullable=False)
    efficiency_score = db.Column(db.Numeric(5, 2), nullable=False)


class RoleType(Enum):
    driver = 'driver'  # 确保与数据库中的枚举值完全匹配
    warehouse = 'warehouse'
    admin = 'admin'


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(SQLEnum(RoleType), nullable=False)  # 使用 SQLAlchemy 的 Enum 类型
    avatar_url = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)  # Simplified enum representation
    load_capacity = db.Column(db.Numeric(10, 2), nullable=False)
    emission_rate = db.Column(db.Numeric(10, 2), nullable=False)
    orders = db.relationship('Order', backref='vehicle')


class Warehouse(db.Model):
    __tablename__ = 'warehouses'
    warehouse_id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Numeric(9, 6), nullable=False)
    latitude = db.Column(db.Numeric(9, 6), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    capacity = db.Column(db.Numeric(10, 2), nullable=False)
