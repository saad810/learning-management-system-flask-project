from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from lms_app.config import Config

# Define your LoginManager instances here
login_manager_user = LoginManager()
login_manager_admin = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions with the app
    db = SQLAlchemy(app)
    bcrypt = Bcrypt(app)
    
    # Import and register blueprints
    from lms_app.main.routes import main
    from lms_app.admin.routes import admin
    from lms_app.users.routes import users
    
    app.register_blueprint(users)
    app.register_blueprint(admin)
    app.register_blueprint(main)
    
    # Initialize the LoginManager instances
    login_manager_user.init_app(app)
    login_manager_user.login_view = 'users.login'
    
    login_manager_admin.init_app(app)
    login_manager_admin.login_view = 'admin.admin_login'
    
    return app
