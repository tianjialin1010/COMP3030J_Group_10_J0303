from sqlalchemy.testing.pickleable import User
from werkzeug.security import generate_password_hash
from backend.App.models import *
from backend.App.models import User
#2024/4/29
from flask import Blueprint,abort,send_from_directory
from werkzeug.security import check_password_hash



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
    return jsonify([{'id': user.user_id, 'name': user.username, 'email': user.email} for user in users])

@blue.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing email or password'}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return jsonify({'success': True, 'message': 'Login successful'}), 200
    else:
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

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

#以下内容用于车牌识别项目
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


@blue.route('/api/delete-items', methods=['POST'])
def delete_items():
    data = request.get_json()
    item_ids = data.get('items', [])

    try:
        for item_id in item_ids:
            item = User.query.filter_by(user_id=item_id).first()
            if item:
                db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Items deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500