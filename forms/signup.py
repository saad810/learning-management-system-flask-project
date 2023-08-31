from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('username',   validators=[
                           DataRequired(message='this field is required')])
    email = StringField('email',         validators=[
                        DataRequired(message='this field is required'), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(message='this field is required')])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(),  EqualTo('confirm_password', message='Passwords must match')])
    submit = SubmitField('Create Account')
