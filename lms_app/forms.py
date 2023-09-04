from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, URLField, MultipleFileField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

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


class CreateCourseForm(FlaskForm):
    title = StringField('Course Title',   validators=[
        DataRequired(message='this field is required')])
    introduction = TextAreaField('Introduction', validators=[
        DataRequired(message='this field is required')])
    description = TextAreaField('Description', validators=[
                                DataRequired(message='type your message here')])
    submit = SubmitField('Create Course')


class CreateCourseModuleForm(FlaskForm):
    title = StringField('Module Title',   validators=[
        DataRequired(message='this field is required')])
    introduction = TextAreaField('Introduce your Module',         validators=[
        DataRequired(message='this field is required')])
    description = TextAreaField('Describe your module', validators=[
                                DataRequired(message='type your message here')])
#    to add resources form field
    video_link = URLField('Enter Youtube Video Link')
    file_upload = MultipleFileField('Module Resources')

    submit = SubmitField('Create Module')


