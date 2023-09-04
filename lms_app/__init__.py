from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "609f7065f62ac95b12c551467d1f68c6"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///lms.db"
db = SQLAlchemy(app)



from lms_app import routes
