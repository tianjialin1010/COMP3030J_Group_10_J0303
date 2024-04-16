import email
from datetime import datetime
from flask import Blueprint, Flask, render_template, request, jsonify, redirect, url_for
from sqlalchemy.testing.pickleable import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import send_file
from backend.App.models import *
import requests
from backend.App.models import User

blue = Blueprint('user', __name__)

@blue.route('/', defaults={'path': 'home'})
@blue.route('/home')
def catch_all(path):
    return render_template("index.html")

# # Route for user login
# # Define a route for the login page
# @blue.route('/api/items')
# def get_items():
#     items = Item.query.all()
#     return jsonify([{'id': item.id, 'name': item.name} for item in items])

@blue.route('/api/customers')
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.user_id,
                     'name': user.username,
                     'email': user.email} for user in users])

@blue.route('/api/orders')
def get_orders():
    orders = Order.query.all()
    orders_data = [{
        'id': order.id,
        'vehicle_id': order.vehicle_id,
        'initiator_user_id': order.initiator_user_id,
        'assigned_driver_id': order.assigned_driver_id,
        'status': order.status,
        'destination': order.destination,
        'mileage': str(order.mileage),
        'created_at': order.created_at.isoformat(),
        'completed_at': order.completed_at.isoformat() if order.completed_at else None,
        'vehicle_type': order.vehicle_type,
        'carbon_emission': str(order.carbon_emission)
    } for order in orders]

    return jsonify(orders_data)
