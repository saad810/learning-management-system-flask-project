from lms_app import db
from lms_app import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
     return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    intro = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Define a relationship with the User model
    user = db.relationship('User', backref=db.backref('courses', lazy=True))

    def __init__(self, title,intro, description, user_id):
        self.title = title
        self.intro = intro
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return f"<Course {self.title}>"