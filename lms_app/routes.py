from flask import render_template, redirect, url_for, flash, request
from lms_app import app, db
from lms_app.forms import (RegisterForm)

@app.route('/')
@app.route('/explore')
def explore():
    return render_template('index.html', title = 'Explore Free Courses')

@app.route('/signup')
def signup():
    form = RegisterForm()
    return render_template('login/signup.html',form = form, title = 'Explore Free Courses')


