import os
from flask import Flask, send_from_directory, session, redirect, url_for
import os
from flask import Flask,send_from_directory
from backend.App.exts import init_exts
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend.App.views import blue
from flask_cors import CORS

import os
from flask import Flask, send_from_directory
from backend.App.exts import init_exts
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend.App.views import blue
from flask_cors import CORS

HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "2003721gavin?"
FLASK_DB = "comp3030j"


def createApp(config_name=None):
    app = Flask(__name__,
                static_folder='../..')  # Ensure this path correctly points to your static files
    CORS(app)
    app.register_blueprint(blueprint=blue)
    app.config['SECRET_KEY'] = 'J0303'
    db_uri = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{FLASK_DB}?charset=utf8mb4'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True  # Simplified configuration, always in debug mode for now

    init_exts(app)  # Initialize other extensions like SQLAlchemy and Migrate
    register_routes(app)  # Setup routes

    return app

def register_routes(app):
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_promo_frontend(path):
        dist_path = os.path.join(app.static_folder, 'frontend-promo', 'dist')
        if path and os.path.exists(os.path.join(dist_path, path)):
            return send_from_directory(dist_path, path)
        else:
            return send_from_directory(dist_path, 'index.html')

    @app.route('/admin/', defaults={'path': ''})
    @app.route('/admin/<path:path>')
    def serve_admin_frontend(path):
        dist_path = os.path.join(app.static_folder, 'frontend-admin', 'dist')
        if path and os.path.exists(os.path.join(dist_path, path)):
            return send_from_directory(dist_path, path)
        else:
            return send_from_directory(dist_path, 'index.html')

    @app.route('/driver/', defaults={'path': ''})
    @app.route('/driver/<path:path>')
    def serve_driver_frontend(path):
        dist_path = os.path.join(app.static_folder, 'frontend-driver', 'dist')
        if path and os.path.exists(os.path.join(dist_path, path)):
            return send_from_directory(dist_path, path)
        else:
            return send_from_directory(dist_path, 'index.html')

    @app.route('/warehouse/', defaults={'path': ''})
    @app.route('/warehouse/<path:path>')
    def serve_warehouse_frontend(path):
        dist_path = os.path.join(app.static_folder, 'frontend-warehouse', 'dist')
        if path and os.path.exists(os.path.join(dist_path, path)):
            return send_from_directory(dist_path, path)
        else:
            return send_from_directory(dist_path, 'index.html')

    # 静态文件处理
    @app.route('/static/<path:filename>')
    def serve_static(filename):
        return app.send_static_file(filename)



