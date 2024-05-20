from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLEnum




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

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(Enum('DRIVER', 'WAREHOUSE', 'ADMIN', name='role_enum'), nullable=False)
    avatar_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    drivers = db.relationship('Driver', backref='user', uselist=False, cascade='all, delete-orphan')
    warehouses = db.relationship('Warehouse', backref='manager', uselist=False, cascade='all, delete-orphan')

class Driver(db.Model):
    __tablename__ = 'drivers'
    driver_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), unique=True, nullable=False)
    total_mileage = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    total_emission = db.Column(db.Numeric(10, 2), nullable=False, default=0.00)
    orders_count = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(Enum('AVAILABLE', 'UNAVAILABLE', name='driver_status_enum'), nullable=False)

    orders = db.relationship('Order', backref='assigned_driver', lazy=True)
    vehicles = db.relationship('Vehicle', backref='owner', lazy=True)

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assigned_driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'), nullable=True)
    status = db.Column(Enum('CREATED', 'ACCEPTED', 'IN_PROGRESS', 'COMPLETED', name='order_status_enum'), nullable=False, default='CREATED')
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    license_plate = db.Column(db.String(10), db.ForeignKey('vehicles.license_plate'), nullable=True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=True)
    completed_at = db.Column(db.TIMESTAMP, nullable=True)
    mileage = db.Column(db.Numeric(10, 2), nullable=True, default=0.00)
    estimate_time = db.Column(db.Numeric(10, 2), nullable=True)
    carbon_emission = db.Column(db.Numeric(10, 2), nullable=True)

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    license_plate = db.Column(db.String(10), primary_key=True, nullable=False)
    type = db.Column(Enum('TRUCK', 'VAN', 'ELECTRIC', name='vehicle_type_enum'), nullable=False)
    emission_rate = db.Column(db.Numeric(10, 2), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'), nullable=False)

    orders = db.relationship('Order', backref='vehicle', lazy=True)

class Warehouse(db.Model):
    __tablename__ = 'warehouses'
    warehouse_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(255), nullable=False)
    capacity = db.Column(db.Numeric(10, 2), nullable=False)
    manager_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)