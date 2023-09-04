from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "609f7065f62ac95b12c551467d1f68c6"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///LMSProject.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


from lms_app import routes
