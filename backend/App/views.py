from sqlalchemy.testing.pickleable import User
from werkzeug.security import generate_password_hash
from backend.App.models import *
from backend.App.models import User
# 2024/4/29
from flask import Blueprint, abort, send_from_directory
from werkzeug.security import check_password_hash
#
from flask import Flask, request, jsonify
import requests
from flask import session  # 引入session

blue = Blueprint('user', __name__)


# @blue.route('/', defaults={'path': 'home'})
# @blue.route('/home')
# def catch_all(path):
#     return render_template("index.html")

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
                     'email': user.email,
                     'role': user.role.value,
                     'created_at': user.created_at,
                     } for user in users])

@blue.route('/api/orders')
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'id': order.order_id,
        'vehicle_id': order.vehicle_id,
        'initiator_user_id': order.initiator_user_id,
        'assigned_driver_id': order.assigned_driver_id,
        'status': order.status.value,
        'destination': order.destination,
        'mileage': float(order.mileage),
        'created_at': order.created_at.isoformat(),
        'completed_at': order.completed_at.isoformat() if order.completed_at else None,
        'vehicle_type': order.vehicle_type,
        'carbon_emission': float(order.carbon_emission),
        'start_location': order.startlocation,
    } for order in orders])


@blue.route('/api/addOrder', methods=['POST'])
def add_order():
    data = request.json
    initiator_user_id = data.get('IU_ID')
    vehicle_type = data.get('vehicle_type')
    destination = data.get('destination')
    start_location = data.get('start_location')

    if not all([initiator_user_id, vehicle_type, destination, start_location]):
        return jsonify({'error': 'Missing data'}), 400

    order = Order(initiator_user_id=initiator_user_id, vehicle_type=vehicle_type, destination=destination, startlocation=start_location)
    db.session.add(order)
    db.session.commit()

    return jsonify({'message': 'Order added successfully'}), 201


@blue.route('/update_order', methods=['POST'])
def update_order():
    data = request.json  # 获取发送过来的 JSON 数据
    ID1 = data.get('ID')

    # 假设你有一个名为 orders 的数据库表
    order = Order.query.filter_by(id=ID1).first()  # 使用 ID 查询订单
    # AD_ID = data.get('AD_ID')
    # Driver_ID = data.get('Driver_ID')
    # Vehicle_ID = data.get('Vehicle_ID')

    if order:
        # 更新订单的其他属性
        order.assigned_driver_id = data.get('AD_ID')
        order.driver = data.get('Driver_ID')
        order.vehicle_id = data.get('Vehicle_ID')

        # 提交更改到数据库
        db.session.commit()

        return jsonify({'message': 'Order updated successfully'}), 200
    else:
        return jsonify({'error': 'Order not found'}), 404


@blue.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        session['user_id'] = user.user_id  # 保存用户ID到session
        session['username'] = user.username  # 保存用户名到session，方便前端显示
        return jsonify({'success': True, 'message': 'Login successful', 'username': user.username}), 200
    else:
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

@blue.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # 清除session
    session.pop('username', None)
    return jsonify({'success': True, 'message': 'Logout successful'}), 200



@blue.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    role = data.get('role')
    password = data.get('password')

    if not email or not name or not role or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=name, email=email, role=role, password_hash=hashed_password, created_at=datetime.utcnow())
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True, 'message': 'User registered successfully'}), 201


# 以下内容用于车牌识别项目
from flask import jsonify, request
import os
from crnn import demo
from flask import Flask, jsonify, request
from crnn.demo import init_model, device, model  # 确保导入了device

# 假设您的图片存放在这个目录下
IMAGE_DIR = os.path.join(os.path.dirname(__file__), '../../crnn/new')


@blue.route('/images', methods=['GET'])
def list_images():
    images = os.listdir(IMAGE_DIR)
    return jsonify(images)


@blue.route('/path_to_images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_DIR, filename)


@blue.route('/recognize', methods=['POST'])
def recognize():
    data = request.json
    if 'image_name' not in data:
        abort(400, description="Missing 'image_name' in request data")
    image_path = os.path.join(IMAGE_DIR, data['image_name'])  # 确保图片在 'new' 目录下
    plate_number = demo.recognize_plate(image_path)
    return jsonify({'plate_number': plate_number})


@blue.route('/api/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    new_password = data.get('new_password')

    if not email or not new_password:
        return jsonify({'error': 'Email and new password are required'}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'No user found with this email'}), 404

    # 更新密码
    user.password_hash = generate_password_hash(new_password)
    db.session.commit()

    return jsonify({'message': 'Password successfully reset'}), 200

@blue.route('/api/delete-orders', methods=['POST'])
def delete_orders():
    data = request.get_json()

    item_ids = data.get('items', [])

    if not item_ids:
        return jsonify({'error': 'No items provided'}), 400  # 如果没有提供任何ID，返回错误

    try:
        for item_id in item_ids:
            item = Order.query.filter_by(order_id=item_id).first()
            if item:
                db.session.delete(item)
            else:
                print(f"No user found with ID: {item_id}")  # 如果没有找到用户，打印这个信息
        db.session.commit()
        return jsonify({'message': 'Items deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@blue.route('/api/delete-users', methods=['POST'])
def delete_users():
    data = request.get_json()

    item_ids = data.get('items', [])

    if not item_ids:
        return jsonify({'error': 'No items provided'}), 400  # 如果没有提供任何ID，返回错误

    try:
        for item_id in item_ids:
            item = User.query.filter_by(user_id=item_id).first()
            if item:
                db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Items deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @blue.route('/api/orders')
# def get_orders():
#     orders = Order.query.all()
#     return jsonify([{
#         'order_id': order.order_id,
#         'vehicle_id': order.vehicle_id,
#         'initiator_user_id': order.initiator_user_id,
#         'assigned_driver_id': order.assigned_driver_id,
#         'status': order.status.value,
#         'destination': order.destination,
#         'mileage': float(order.mileage),
#         'created_at': order.created_at.isoformat(),
#         'completed_at': order.completed_at.isoformat() if order.completed_at else None,
#         'vehicle_type': order.vehicle_type,
#         'carbon_emission': float(order.carbon_emission),
#         } for order in orders])


@blue.route('/api/weather')
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    api_key = 'b2ebe693daf761902632f26c202f9a1d'
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    weather = {
        'temp_min': data['main']['temp_min'],
        'temp_max': data['main']['temp_max'],
        'description': data['weather'][0]['description']
    }
    return jsonify(weather)
