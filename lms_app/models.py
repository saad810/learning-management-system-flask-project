from lms_app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    acc_type = db.Column(db.String(30), nullable=False)
    acc_status = db.Column(db.Integer, nullable=False, default = 0)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, add_type = {self.acc_type})>"
    
class Contact(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True)
    message = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"<Contact(id={self.id}, name={self.name}, email={self.email}, message = {self.message})>"
    