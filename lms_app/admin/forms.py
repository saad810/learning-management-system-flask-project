from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, URLField, MultipleFileField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('username',   validators=[
                           DataRequired(message='this field is required')])

    password = PasswordField('Password', validators=[
                             DataRequired(message='this field is required')])

    submit = SubmitField('Login')


class CreateCourseForm(FlaskForm):
    title = StringField('Name',   validators=[
        DataRequired(message='this field is required')])
    introduction = TextAreaField('Email',         validators=[
        DataRequired(message='this field is required')])
    description = TextAreaField('Your Message', validators=[
                                DataRequired(message='type your message here')])
    submit = SubmitField('Create Course')


class CreateCourseModuleForm(FlaskForm):
    title = StringField('Name',   validators=[
        DataRequired(message='this field is required')])
    introduction = TextAreaField('Email',         validators=[
        DataRequired(message='this field is required')])
    description = TextAreaField('Your Message', validators=[
                                DataRequired(message='type your message here')])
#    to add resources form field

    submit = SubmitField('Create Course')


class Resourses(FlaskForm):
    video_link = URLField('Enter Youtube Video Link')
    file_upload = MultipleFileField('Module Resources')
    submit = SubmitField('Add Resources')
