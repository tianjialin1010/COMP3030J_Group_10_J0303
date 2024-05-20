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

import random
import string
from flask import send_file, session
from captcha.image import ImageCaptcha
import io

blue = Blueprint('user', __name__)

def generate_random_captcha(length=4):
    # 生成一个包含大写字母和数字的验证码
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

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
def get_customers():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    customers_query = User.query.paginate(page=page, per_page=per_page, error_out=False)
    total = customers_query.total
    customers = customers_query.items

    return jsonify({
        'total': total,
        'users': [{
            'id': user.user_id,
            'name': user.username,
            'email': user.email,
            'role': user.role,
            'created_at': user.created_at.isoformat() if user.created_at else None
        } for user in customers]
    })


@blue.route('/api/orders')
def get_orders():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    orders_query = Order.query.paginate(page=page, per_page=per_page, error_out=False)
    total = orders_query.total
    orders = orders_query.items

    return jsonify({
        'total': total,
        'orders': [{
            'id': order.order_id,
            'assigned_driver_id': order.assigned_driver_id,
            'status': order.status,
            'origin': order.origin,
            'destination': order.destination,
            'license_plate': order.license_plate,
            'created_at': order.created_at.isoformat() if order.created_at else None,
            'completed_at': order.completed_at.isoformat() if order.completed_at else None,
            'mileage': float(order.mileage) if order.mileage is not None else None,
            'estimate_time': float(order.estimate_time) if order.estimate_time is not None else None,
            'carbon_emission': float(order.carbon_emission) if order.carbon_emission is not None else None
        } for order in orders]
    })



@blue.route('/api/addOrder', methods=['POST'])
def add_order():
    data = request.json
    origin = data.get('origin')
    destination = data.get('destination')
    mileage = data.get('mileage', 0.00)  # 默认值为 0.00
    estimate_time = data.get('estimate_time')  # 可以为空

    # 检查必要字段是否存在
    if not all([origin, destination,mileage,estimate_time]):
        return jsonify({'error': 'Missing data'}), 400

    # 创建 Order 实例
    order = Order(
        origin=origin,
        destination=destination,
        mileage=mileage,
        estimate_time=estimate_time,
        created_at=datetime.utcnow()
    )

    # 添加到数据库会话并提交
    db.session.add(order)
    db.session.commit()

    return jsonify({'message': 'Order added successfully'}), 201


@blue.route('/update_order', methods=['POST'])
def update_order():
    data = request.json
    order_id = data.get('order_id')

    # 获取当前登录用户的 user_id
    user_id = session.get('user_id')

    # 根据 user_id 查找 driver_id
    driver = Driver.query.filter_by(user_id=user_id).first()

    if not driver:
        return jsonify({'error': 'You are not a driver'}), 403

    driver_id = driver.driver_id

    # 查找订单
    order = Order.query.filter_by(order_id=order_id).first()

    if not order:
        return jsonify({'error': 'Order not found'}), 404

    # 更新订单信息
    order.assigned_driver_id = driver_id
    order.status = 'ACCEPTED'
    order.license_plate = data.get('vehicle_id')
    order.created_at = datetime.utcnow()

    db.session.commit()

    return jsonify({'message': 'Order updated successfully'}), 200

@blue.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    user_id = session.get('user_id')

    driver = Driver.query.filter_by(user_id=user_id).first()
    if not driver:
        return jsonify({'error': 'You are not a driver'}), 403

    vehicles = Vehicle.query.filter_by(owner_id=driver.driver_id).all()
    vehicle_list = [{'license_plate': vehicle.license_plate} for vehicle in vehicles]

    return jsonify(vehicle_list)



@blue.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    if 'captcha' in data and session.get('captcha', '') == data['captcha']:
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.user_id  # 保存用户ID到session
            session['username'] = user.username  # 保存用户名到session，方便前端显示
            return jsonify({'success': True, 'message': 'Login successful', 'username': user.username}), 200
        else:
            return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

        pass

    else:
        return jsonify({'error': 'Invalid captcha'}), 400

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

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to register user', 'details': str(e)}), 500

    if role == 'DRIVER':
        new_driver = Driver(user_id=new_user.user_id, total_mileage=0.00, total_emission=0.00, orders_count=0,
                            status='AVAILABLE')
        try:
            db.session.add(new_driver)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': 'Failed to create driver record', 'details': str(e)}), 500

    return jsonify({'success': True, 'message': 'User registered successfully'}), 201


# 以下内容用于车牌识别项目
from flask import jsonify, request
import os
from crnn import demo
from flask import Flask, jsonify, request
from crnn.demo import init_model, device, model  # 确保导入了device

# 假设您的图片存放在这个目录下
# IMAGE_DIR = os.path.join(os.path.dirname(__file__), '../../crnn/new')


# @blue.route('/images', methods=['GET'])
# def list_images():
#     images = os.listdir(IMAGE_DIR)
#     return jsonify(images)
#
#
# @blue.route('/path_to_images/<filename>')
# def serve_image(filename):
#     return send_from_directory(IMAGE_DIR, filename)
#
#
# @blue.route('/recognize', methods=['POST'])
# def recognize():
#     data = request.json
#     if 'image_name' not in data:
#         abort(400, description="Missing 'image_name' in request data")
#     image_path = os.path.join(IMAGE_DIR, data['image_name'])  # 确保图片在 'new' 目录下
#     plate_number = demo.recognize_plate(image_path)
#     return jsonify({'plate_number': plate_number})


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
            item = User.query.get(item_id)
            if item:
                db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Items deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
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



@blue.route('/api/captcha')
def generate_captcha():
    image = ImageCaptcha(width=280, height=90)
    captcha_text = generate_random_captcha()  # 生成随机的验证码文本
    data = image.generate(captcha_text)
    session['captcha'] = captcha_text  # 将验证码文本保存在session中以供验证
    return send_file(io.BytesIO(data.getvalue()), mimetype='image/png')


# In Flask, receiving and processing data:
@blue.route('/api/endOrder', methods=['POST'])
def end_order():
    data = request.json
    mileage = data.get('Mileage')
    vehicle_id = data.get('Vehicle_ID')
    plate_number = data.get('PlateNumber')  # You are receiving it but not using it
    completed_at = datetime.utcnow()  # Server time, no need to send from client

    if not all([mileage, vehicle_id]):
        return jsonify({'error': 'Missing data'}), 400

    order = Order.query.filter_by(vehicle_id=vehicle_id).first()
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    order.mileage = mileage
    order.completed_at = completed_at
    carbon_emission = float(mileage) * 0.2
    order.carbon_emission = carbon_emission

    db.session.commit()

    return jsonify({'message': 'Order updated successfully', 'carbon_emission': carbon_emission}), 200

@blue.route('/video')
def get_video():
    return send_file('../../frontend/src/assets/images/test.mp4', mimetype='video/mp4')

@blue.route('/api/<path:filename>')
def get_model(filename):
    return send_from_directory('../3d/', filename)


IMAGE_DIR = '../../crnn/new'  # 确保路径正确


@blue.route('/api/images', methods=['GET'])
def get_images():
    images = os.listdir(IMAGE_DIR)
    return jsonify(images)


@blue.route('/api/images/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(IMAGE_DIR, filename)


@blue.route('/api/recognize', methods=['POST'])
def recognize():
    if 'image' not in request.files:
        abort(400, description="Missing 'image' in request files")
    image = request.files['image']
    image_path = os.path.join(IMAGE_DIR, image.filename)
    image.save(image_path)

    plate_number = demo.recognize_plate(image_path)
    return jsonify({'plate_number': plate_number})