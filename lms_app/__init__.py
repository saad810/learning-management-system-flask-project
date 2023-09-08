from flask import Flask
from flask_bcrypt import Bcrypt
from lms_app.utils.database import DBconnector

app = Flask(__name__)
app.config['SECRET_KEY'] = "609f7065f62ac95b12c551467d1f68c6"
bcrypt = Bcrypt(app)

db = DBconnector()

from lms_app import routes
