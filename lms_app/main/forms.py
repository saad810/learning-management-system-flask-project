from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email



class ContactForm(FlaskForm):
    name = StringField('Name',   validators=[
        DataRequired(message='this field is required')])
    email = StringField('Email',         validators=[
                        DataRequired(message='this field is required'), Email()])
    message = TextAreaField('Your Message', validators=[
                            DataRequired(message='type your message here')])
    submit = SubmitField('Send Message')
