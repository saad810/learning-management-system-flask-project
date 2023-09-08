from flask import render_template, redirect, url_for, flash, request, session
from lms_app import app, db, bcrypt
from lms_app.forms import (RegisterForm, LoginForm,
                           CreateCourseForm, CreateCourseModuleForm, AddSubjectForm)
from lms_app.utils.functions import (
    check_duplicate_username, get_subjects, check_duplicate_email, check_user)


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
        if check_duplicate_username(username) == True:
            flash('Username already taken. Please choose another one.')
            return redirect(url_for('signup'))

        if check_duplicate_email(email) == True:
            flash('Username already taken. Please choose another one.')
            return redirect(url_for('signup'))
        else:
            query = "insert into person (username,email,password)values( %s, %s, %s )"
            values = (username, email, hashed_password)
            db.execute_query(query, values)

            flash('Registration successful! Please Login')
            return redirect(url_for('login'))

    return render_template('login/signup.html', form=form, title='Start a Learning Journey')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_exists = check_user(form.username.data)
        if user_exists:
            flash('Login Successful')
            session['user'] = form.username.data
            session['logged_in'] = True
            return redirect(url_for('user_home'))
        else:
            flash('User Does not exists')
            return redirect('login')

    return render_template('login/login.html', form=form, title='Welcome Back')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if "user" in session:
        session.pop("user", None)
        session['logged_in'] = False
        flash('Logout successfull')
    else:
        flash('you are not logged in')

    return redirect(url_for('login'))


@app.route('/user', methods=['GET', 'POST'])
# @login_required
def user_home():
    if "user" in session and session["logged_in"] == True:
        return render_template('protected_user/index.html', title='Start Learning')
    else:
        flash("you need to login first")
        return redirect('login')


# creating courses
@app.route('/user/create-course', methods=['GET', 'POST'])
# @login_required
def user_create_course():
    if "user" not in session and session["logged_in"] == False:
        flash("you need to login first")
        return redirect('login')

    form = CreateCourseForm()
    value = get_subjects()
    
    # if form.validate_on_submit() and request.method == 'POST':

    #     title = form.title.data
    #     intro = form.introduction.data
    #     description = form.description.data
    #     user = session["user"]
    #     if title and description and intro and user:
    #         course_query = "insert into courses (title)values( %s)"
    #         values = (title)
    #         db.execute_query(course_query, values)
    #         course_no = get_course_id(title)
    #         info_query = "insert into course_info (title)values( %s)"
    #         values = (title)
    #         db.execute_query(info_query, values)
    #         flash('Course Creation successful! Please Create Modules')
    #         return redirect(url_for('user_create_module'))

    # else:
    #     flash('Invalid course data. Please check your inputs.', 'danger')

    return render_template('create_course/create_course.html', form=form, data=value, title='Create Course')


@app.route('/user/add-subjects', methods=['POST', 'GET'])
def add_subject():
    if "user" not in session and session["logged_in"] == False:
        flash("you need to login first")
        return redirect('login')
    else:
        form = AddSubjectForm()
        if form.validate_on_submit() and request.method == 'POST':
            query = "insert into subjects (sub_name) values (%s) "
            values = (form.title.data,)
            db.execute_query(query, values)
            flash('Subject Added Successfully')
            return redirect(url_for('add_subject'))
        return render_template('create_course/add_subject.html', form=form, title='Add Subject')


# creating courses
@app.route('/user/create-module', methods=['GET', 'POST'])
# @login_required
def user_create_module():
    form = CreateCourseModuleForm()
    # resources = ModuleResoursesForm()
    return render_template(
        'create_course/create_module.html',
        title='Create Module',
        form=form
        # resoures = resources
    )
