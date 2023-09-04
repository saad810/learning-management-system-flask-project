from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import (DataRequired, Email, EqualTo)


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


class LoginForm(FlaskForm):
    username = StringField('username',   validators=[
                           DataRequired(message='this field is required')])

    password = PasswordField('Password', validators=[
                             DataRequired(message='this field is required')])

    submit = SubmitField('Login')


class RequestAccForm(FlaskForm):
    username = StringField('username',   validators=[
                           DataRequired(message='this field is required')])
    email = StringField('email',         validators=[
                        DataRequired(message='this field is required'), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(message='this field is required')])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(),  EqualTo('confirm_password', message='Passwords must match')])
    message = TextAreaField('Reason of Request', validators=[
                            DataRequired(message='type your message here')])
    submit = SubmitField('Request Account')

