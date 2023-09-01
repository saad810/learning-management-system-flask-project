from flask import Flask 
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = "530808f4d10604d7cf44b03bee21f246"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///LMS_app_project.db"
db = SQLAlchemy(app)

from lms_app import routes