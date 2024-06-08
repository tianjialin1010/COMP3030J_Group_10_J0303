# views.py
from datetime import datetime, timedelta
from sqlalchemy.testing.pickleable import User
from werkzeug.security import generate_password_hash
from backend.App.models import *
from backend.App.models import User
# 2024/4/29
from flask import Blueprint, abort, send_from_directory, url_for
from werkzeug.security import check_password_hash
from flask import Flask, request, jsonify
import requests
from backend.uploads.avatars import *
import random
import string
from flask import send_file, session, current_app
from captcha.image import ImageCaptcha
import io
from flask import Blueprint, request, jsonify, Response

blue = Blueprint('user', __name__)

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
            'created_at': user.created_at.isoformat() if user.created_at else None,
            'avatar_url': url_for('user.serve_avatar', filename=user.avatar_url, _external=True) if user.avatar_url else None,
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


@blue.route('/api/update_order', methods=['POST'])
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



# @blue.route('/api/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#
#     if not email or not password:
#         return jsonify({'error': 'Missing email or password'}), 400
#
#     if 'captcha' in data and session.get('captcha', '') == data['captcha']:
#         user = User.query.filter_by(email=email).first()
#         if user and check_password_hash(user.password_hash, password):
#             session['user_id'] = user.user_id  # 保存用户ID到session
#             session['username'] = user.username  # 保存用户名到session，方便前端显示
#             return jsonify({'success': True, 'message': 'Login successful', 'username': user.username}), 200
#         else:
#             return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
#
#         pass
#
#     else:
#         return jsonify({'error': 'Invalid captcha'}), 400




# def generate_random_captcha(length=4):
#     # 生成一个包含大写字母和数字的验证码
#     characters = string.ascii_uppercase + string.digits
#     return ''.join(random.choice(characters) for _ in range(length))
#
#
# @blue.route('/api/captcha')
# def generate_captcha():
#     image = ImageCaptcha(width=280, height=90)
#     captcha_text = generate_random_captcha()
#     data = image.generate(captcha_text)
#     session['captcha'] = captcha_text  # 将验证码保存到 session 中
#     return send_file(io.BytesIO(data.getvalue()), mimetype='image/png')
#
#
# @blue.route('/api/login', methods=['POST'])
# def user_login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#
#     if not email or not password:
#         return jsonify({'error': 'Missing email or password'}), 400
#
#     if 'captcha' in data and session.get('captcha', '') == data['captcha']:
#         user = User.query.filter_by(email=email).first()
#         if user and check_password_hash(user.password_hash, password):
#             session.clear()  # 登录前先清除现有会话
#             session['user_id'] = user.user_id  # 保存用户ID到session
#             session['username'] = user.username  # 保存用户名到session，方便前端显示
#             session['role'] = user.role  # 保存用户角色到session
#
#             # 根据角色返回不同的前端URL
#             if user.role == 'DRIVER':
#                 return jsonify({'success': True, 'message': 'Login successful', 'username': user.username, 'redirect_url': '/driver'})
#             elif user.role == 'WAREHOUSE':
#                 return jsonify({'success': True, 'message': 'Login successful', 'username': user.username, 'redirect_url': '/warehouse'})
#             elif user.role == 'ADMIN':
#                 return jsonify({'success': True, 'message': 'Login successful', 'username': user.username, 'redirect_url': '/admin'})
#             else:
#                 return jsonify({'success': False, 'error': 'Invalid role'}), 401
#         else:
#             return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
#     else:
#         return jsonify({'error': 'Invalid captcha'}), 400
#
#
#
# @blue.route('/api/logout', methods=['POST'])
# def user_logout():
#     session.clear()  # 清除所有会话信息
#     return jsonify({'success': True, 'message': 'Logout successful', 'redirect_url': '/'})
#
#
# @blue.route('/api/user-session', methods=['GET'])
# def get_user_session():
#     user_id = session.get('user_id')
#     username = session.get('username')
#     role = session.get('role')
#     if user_id and username and role:
#         return jsonify({'user_id': user_id, 'username': username, 'role': role}), 200
#     else:
#         return jsonify({'error': 'No active session found'}), 404

from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash
from backend.App.models import User
import random
import string
from captcha.image import ImageCaptcha
import io

def generate_random_captcha(length=4):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@blue.route('/api/captcha')
def generate_captcha():
    image = ImageCaptcha(width=280, height=90)
    captcha_text = generate_random_captcha()
    data = image.generate(captcha_text)
    session['captcha'] = captcha_text
    return send_file(io.BytesIO(data.getvalue()), mimetype='image/png')

@blue.route('/api/login', methods=['POST'])
def user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    if 'captcha' in data and session.get('captcha', '') == data['captcha']:
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session.clear()  # 登录前先清除现有会话
            session['user_id'] = user.user_id  # 保存用户ID到session
            session['username'] = user.username  # 保存用户名到session，方便前端显示
            session['role'] = user.role  # 保存用户角色到session

            # 根据角色返回不同的前端URL
            if user.role == 'DRIVER':
                return jsonify({'success': True, 'message': 'Login successful', 'user': user.username, 'redirect_url': '/driver'})
            elif user.role == 'WAREHOUSE':
                return jsonify({'success': True, 'message': 'Login successful', 'user': user.username, 'redirect_url': '/warehouse'})
            elif user.role == 'ADMIN':
                return jsonify({'success': True, 'message': 'Login successful', 'user': user.username, 'redirect_url': '/admin'})
            else:
                return jsonify({'success': False, 'error': 'Invalid role'}), 401
        else:
            return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'Invalid captcha'}), 400


@blue.route('/api/logout', methods=['POST'])
def user_logout():
    session.clear()  # 清除所有会话信息
    return jsonify({'success': True, 'message': 'Logout successful'})


@blue.route('/api/user-session', methods=['GET'])
def get_user_session():
    user_id = session.get('user_id')
    username = session.get('username')
    role = session.get('role')
    if user_id and username and role:
        return jsonify({'user_id': user_id, 'username': username, 'role': role}), 200
    else:
        return jsonify({'error': 'No active session found'}), 404



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


# In Flask, receiving and processing data:
@blue.route('/api/end_order', methods=['POST'])
def end_order():
    data = request.json
    license_plate = data.get('license_plate')

    if not license_plate:
        return jsonify({'error': 'Missing license_plate'}), 400

    orders = Order.query.filter_by(license_plate=license_plate).all()

    if not orders:
        return jsonify({'error': 'No orders found with this license plate'}), 404

    for order in orders:
        order.status = 'COMPLETED'
        order.completed_at = datetime.utcnow()
        # 找到绑定司机并更新状态
        driver = Driver.query.filter_by(driver_id=order.assigned_driver_id).first()
        if driver:
            driver.status = 'AVAILABLE'

    db.session.commit()

    return jsonify({'message': f'{len(orders)} order(s) ended successfully'}), 200

@blue.route('/video')
def get_video():
    return send_file('../../frontend-driver/src/assets/images/test.mp4', mimetype='video/mp4')


from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify, send_from_directory, abort
import os
from crnn import demo  # 确保导入正确的识别函数


IMAGE_DIR = '../../crnn/new'  # 确保路径正确

# 确保 IMAGE_DIR 路径存在
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

@blue.route('/api/images', methods=['GET'])
def get_images():
    try:
        images = os.listdir(IMAGE_DIR)
        return jsonify(images)
    except Exception as e:
        print(f"Error listing images: {e}")
        return jsonify({'error': 'Failed to list images', 'details': str(e)}), 500

@blue.route('/api/images/<filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory(IMAGE_DIR, filename)
    except Exception as e:
        print(f"Error serving image {filename}: {e}")
        return jsonify({'error': 'File not found', 'details': str(e)}), 404

@blue.route('/api/recognize', methods=['POST'])
def recognize():
    try:
        if 'image' in request.files:
            image = request.files['image']
            if image.filename == '':
                abort(400, description="No selected file")

            filename = secure_filename(image.filename)
            image_path = os.path.join(IMAGE_DIR, filename)
            image.save(image_path)

        elif 'image_name' in request.form:
            image_name = request.form['image_name']
            image_path = os.path.join(IMAGE_DIR, image_name)
            if not os.path.exists(image_path):
                abort(400, description="Image not found")
        else:
            abort(400, description="No image provided")

        # 调用车牌识别函数
        plate_number = demo.recognize_plate(image_path)

        # 返回识别结果
        return jsonify({'plate_number': plate_number})

    except Exception as e:
        # 捕获所有异常并返回 500 错误
        print(f"Error processing request: {e}")
        return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500

# 以下内容是关于可持续性分析报告的：
@blue.route('/api/driver-info', methods=['GET'])
def get_driver_info():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'No user logged in'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if user.role != 'DRIVER':
        return jsonify({'error': 'User is not a driver'}), 403

    driver = Driver.query.filter_by(user_id=user_id).first()
    if not driver:
        return jsonify({'error': 'Driver not found'}), 404

    # Calculate the total carbon emission
    total_carbon_emission = sum(order.carbon_emission for order in driver.orders if order.carbon_emission is not None)

    driver_info = {
        'username': user.username,
        'email': user.email,
        'avatar_url': user.avatar_url,
        'total_mileage': driver.total_mileage,
        'total_emission': driver.total_emission,
        'orders_count': driver.orders_count,
        'status': driver.status,
        'total_carbon_emission': total_carbon_emission
    }

    return jsonify(driver_info), 200


@blue.route('/api/user-info', methods=['GET'])
def get_user_info():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'No user logged in'}), 401
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user_info = {
        'username': user.username,
        'role': user.role,
        'avatar_url': url_for('user.serve_avatar', filename=user.avatar_url, _external=True)
    }
    return jsonify(user_info), 200



# 使用相对路径构建 UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@blue.route('/api/upload-avatar', methods=['POST'])
def upload_avatar():
    if 'avatar' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['avatar']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        # 使用 current_app 在请求处理函数内部获取应用实例的根路径
        upload_folder = os.path.join(current_app.root_path, 'uploads', 'avatars')
        os.makedirs(upload_folder, exist_ok=True)  # 确保目录存在

        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'No user logged in'}), 401

        # 使用用户 ID 作为文件名
        filename = f'user_{user_id}.png'
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)

        # 更新用户头像路径
        # 假设有一个User模型和db.session
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user.avatar_url = filename
        db.session.commit()

        return jsonify({'message': 'Avatar uploaded successfully', 'avatar_url': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400


@blue.route('/api/avatars/<filename>')
def serve_avatar(filename):
    directory = os.path.join(current_app.root_path, 'uploads', 'avatars')
    try:
        return send_from_directory(directory, filename)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

@blue.route('/api/users', methods=['GET'])
def get_users():
    user_list = User.query.all()  # 获取所有用户
    users_data = []
    for user in user_list:
        driver_info = Driver.query.filter_by(user_id=user.user_id).first()
        user_data = {
            'id': user.user_id,
            'username': user.username,
            'avatar_url': user.avatar_url if user.avatar_url else 'path/to/default/avatar.jpg',  # 提供默认头像路径
            'role': user.role,
            'status': 'Available' if driver_info and driver_info.status == 'AVAILABLE' else 'Unavailable',
            'totalMileage': driver_info.total_mileage if driver_info else 0
        }
        users_data.append(user_data)
    return jsonify(users_data)


@blue.route('/api/update-user-info', methods=['POST'])
def update_user_info():
    data = request.json
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    username = data.get('username')
    email = data.get('email')

    if username:
        user.username = username
    if email:
        user.email = email

    db.session.commit()
    return jsonify({'message': 'User info updated successfully'}), 200


@blue.route('/api/carbon-emission', methods=['GET'])
def get_carbon_emission():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'No user logged in'}), 401

    # 获取当前时间和六个月前的时间
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=6 * 30)

    # 查询过去六个月内的订单数据
    orders = Order.query.filter(Order.created_at.between(start_date, end_date),
                                Order.assigned_driver_id == user_id).all()

    # 计算总碳排放量
    your_emissions = sum(order.carbon_emission for order in orders if order.carbon_emission is not None)
    expected_emissions = sum(
        order.estimate_time * Vehicle.query.filter_by(license_plate=order.license_plate).first().emission_rate for order
        in orders if order.estimate_time is not None)
    colleagues_emissions = sum(
        order.carbon_emission for order in Order.query.filter(Order.created_at.between(start_date, end_date)).all() if
        order.carbon_emission is not None)

    # 返回数据
    return jsonify({
        'your_emissions': your_emissions,
        'expected_emissions': expected_emissions,
        'colleagues_emissions': colleagues_emissions,
        'average_emissions': colleagues_emissions / 6  # 假设过去六个月的总数据
    })

CAR_IMAGE_DIR = '../images/Cars'

@blue.route('/api/car_images/<filename>', methods=['GET'])
def get_car_image(filename):
    try:
        return send_from_directory(CAR_IMAGE_DIR, filename)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404


@blue.route('/api/recent-orders', methods=['GET'])
def get_recent_orders():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    driver = Driver.query.filter_by(user_id=user_id).first()
    if not driver:
        return jsonify({'error': 'Driver not found'}), 404

    orders = (Order.query
              .filter_by(assigned_driver_id=driver.driver_id)
              .order_by(Order.completed_at.desc())
              .limit(10)
              .all())

    if not orders:
        return jsonify({'error': 'No orders found'}), 404

    recent_orders = []
    for order in orders:
        vehicle = Vehicle.query.filter_by(license_plate=order.license_plate, type='ELECTRIC').first()
        if vehicle:
            if order.mileage is not None and vehicle.emission_rate is not None:
                expected_emission = float(order.mileage) * float(vehicle.emission_rate) * 100
                if order.carbon_emission is not None and float(order.carbon_emission) < expected_emission:
                    recent_orders.append({
                        'origin': order.origin,
                        'destination': order.destination,
                        'vehicle_type': vehicle.type,
                        'completed_at': order.completed_at.strftime('%Y-%m-%d'),
                        'carbon_saving': float(expected_emission - float(order.carbon_emission))
                    })

    if not recent_orders:
        return jsonify({'error': 'No orders with better emissions'}), 404

    return jsonify(recent_orders)

@blue.route('/api/recent-orders-worst', methods=['GET'])
def get_recent_orders_worst():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    driver = Driver.query.filter_by(user_id=user_id).first()
    if not driver:
        return jsonify({'error': 'Driver not found'}), 404

    # 过滤条件：车型不是ELECTRIC，订单结束日期不早于2023年9月，订单完成日期不是2024年5月5日
    orders = Order.query.filter(
        Order.assigned_driver_id == driver.driver_id,
        Order.completed_at <= datetime(2023, 11, 1)
    ).order_by(Order.completed_at.desc()).limit(10).all()

    recent_orders_worst = []
    for order in orders:
        vehicle = Vehicle.query.filter_by(license_plate=order.license_plate).first()
        if vehicle and vehicle.type != 'ELECTRIC':
            expected_emission = float(order.mileage) * float(vehicle.emission_rate)*0.1
            if float(order.carbon_emission) > expected_emission:
                recent_orders_worst.append({
                    'order_id': order.order_id,
                    'origin': order.origin,
                    'destination': order.destination,
                    'vehicle_type': vehicle.type,
                    'completed_at': order.completed_at.strftime('%Y-%m-%d'),
                    'carbon_wasting': float(order.carbon_emission) - expected_emission
                })

    return jsonify(recent_orders_worst)

@blue.route('/api/get_driver_id', methods=['GET'])
def get_driver_id():
    user_id = session.get('user_id')  # 假设 session 中保存了 user_id
    if not user_id:
        return jsonify({'error': 'User not logged in'}), 401

    driver = Driver.query.filter_by(user_id=user_id).first()
    if not driver:
        return jsonify({'error': 'Driver not found'}), 404

    return jsonify({'driver_id': driver.driver_id})


@blue.route('/backend/3d/<path:filename>')
def serve_glb(filename):
    return send_from_directory('../3d', filename)

@blue.route('/api/recent-orders', methods=['GET'])
def dashboard_get_recent_orders():
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({'error': 'User not logged in'}), 401

        driver = Driver.query.filter_by(user_id=user_id).first()
        if not driver:
            return jsonify({'error': 'User is not a driver'}), 403

        try:
            recent_orders = Order.query.filter_by(assigned_driver_id=driver.driver_id).order_by(
                Order.created_at.desc()).limit(5).all()

            orders_data = []
            for order in recent_orders:
                order_data = {
                    'order_id': order.order_id,
                    'status': order.status,
                    'origin': order.origin,
                    'destination': order.destination,
                    'created_at': order.created_at.isoformat() if order.created_at else None,
                    'completed_at': order.completed_at.isoformat() if order.completed_at else None,
                }
                # Handle potential NoneType and decimal.Decimal issues
                if order.mileage is not None:
                    order_data['mileage'] = float(order.mileage)
                if order.estimate_time is not None:
                    order_data['estimate_time'] = float(order.estimate_time)
                if order.carbon_emission is not None:
                    order_data['carbon_emission'] = float(order.carbon_emission)

                orders_data.append(order_data)

            return jsonify(orders_data)

        except Exception as e:
            return jsonify({'error': 'Internal Server Error'}), 500



