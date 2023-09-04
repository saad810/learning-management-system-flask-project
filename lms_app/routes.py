from flask import render_template, redirect, url_for, flash, request
from lms_app import app, db, bcrypt
from lms_app.forms import (RegisterForm, LoginForm,
                           CreateCourseForm, CreateCourseModuleForm)
from lms_app.models import (User, Course)
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/explore')
def explore():
    return render_template('index.html', title='Explore Free Courses')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password, 10)

        # Check for duplicate email or username

        duplicate_username = User.query.filter_by(username=username).first()

        if duplicate_username:
            flash('Username already taken. Please choose another one.')
            return redirect(url_for('signup'))

        try:
            user = User(
                username=username,
                email=email,
                password=hashed_password,
            )
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please Login')
            return redirect(url_for('explore'))

        except Exception as e:
            # Handle any other exceptions that might occur during registration
            db.session.rollback()  # Rollback the transaction
            flash('An error occurred during registration.')
            return redirect(url_for('signup'))

    return render_template('login/signup.html', form=form, title='Start a Learning Journey')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user:
            #  check hash
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Login Successfull')
                return redirect(url_for('user_home'))
            else:
                flash('Wrong username or password')
        else:
            flash('Login Not Allowed')
            return redirect(url_for('login'))

    return render_template('login/login.html', form=form, title='Welcome Back')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('Logout successfull')
    return redirect(url_for('login'))


@app.route('/user', methods=['GET', 'POST'])
@login_required
def user_home():
    return render_template('protected_user/index.html', title='Start Learning')


# creating courses
@app.route('/user/create-course', methods=['GET', 'POST'])
@login_required
def user_create_course():
    form = CreateCourseForm()
    if form.validate_on_submit() and request.method == 'POST':
        title = form.title.data
        intro = form.introduction.data
        description = form.description.data
        user_id = current_user.id
        if title and description and intro and user_id >= 1:
            add_course = Course(
                title=title,
                intro=intro,
                description=description,
                user_id=user_id
            )
            db.session.add(add_course)
            db.session.commit()
            flash('Course Creation successful! Please Create Modules')
            return redirect(url_for('user_create_module'))

    else:
        flash('Invalid course data. Please check your inputs.', 'danger')

    return render_template('create_course/create_course.html', form=form, title='Create Course')


# creating courses
@app.route('/user/create-module', methods=['GET', 'POST'])
@login_required
def user_create_module():
    form = CreateCourseModuleForm()
    # resources = ModuleResoursesForm()
    return render_template(
        'create_course/create_module.html',
        title='Create Module',
        form=form
        # resoures = resources
    )
