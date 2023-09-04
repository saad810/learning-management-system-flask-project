from flask import Blueprint, redirect, url_for, flash, render_template
from lms_app.users.forms import RegisterForm,  LoginForm
from flask_login import login_required, login_user, logout_user
from lms_app.models import User
from lms_app import db, bcrypt


users = Blueprint('users', __name__)


# global home route


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password, 10)
        acc_type = "A"
        acc_status = 1

        # Check for duplicate email or username

        duplicate_username = User.query.filter_by(username=username).first()

        if duplicate_username:
            flash('Username already taken. Please choose another one.')
            return redirect(url_for('users.signup'))

        try:
            user = User(
                username=username,
                email=email,
                password=hashed_password,
                acc_type=acc_type,
                acc_status=acc_status
            )
            db.session.add(user)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for('users.login'))

        except Exception as e:
            # Handle any other exceptions that might occur during registration
            db.session.rollback()  # Rollback the transaction
            flash('An error occurred during registration.')
            return redirect(url_for('users.signup'))

    return render_template('client/signup.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_acc_appproved = User.query.filter_by(acc_status='2').first()
        user = User.query.filter_by(username=form.username.data).first()
        users_with_user_acc = User.query.filter_by(acc_type='U').all()
        if users_with_user_acc and user_acc_appproved:

            if user:
                #  check hash
                if bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    flash('Login Successfull')
                    return redirect(url_for('users.user_home'))
                else:
                    flash('Wrong username or password')
            else:
                flash('Wrong username or password')
            # else:
        else:
            flash('Login Not Allowed')
            return redirect(url_for('users.login'))

    return render_template('client/login.html', form=form)


# logout route


@users.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    flash('Logout successfull')
    return redirect(url_for('users.login'))


# user protected routes

@users.route('/user-dash')
@login_required
def user_home():
    return render_template('client/protected_client/index.html')

# account request for admin


@users.route('/admin/acc-req', methods=['GET', 'POST'])
def admin_acc_request():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password, 10)
        acc_type = "A"
        acc_status = 0

        # Check for duplicate email or username

        duplicate_username = User.query.filter_by(username=username).first()

        if duplicate_username:
            flash('Username already taken. Please choose another one.')
            return redirect(url_for('users.signup'))

        try:
            user = User(
                username=username,
                email=email,
                password=hashed_password,
                acc_type=acc_type,
                acc_status=acc_status
            )
            db.session.add(user)
            db.session.commit()
            flash('Wait for Approval Email')
            return redirect(url_for('users.login'))

        except Exception as e:
            # Handle any other exceptions that might occur during registration
            db.session.rollback()  # Rollback the transaction
            flash('An error occurred during Form Submition.')
            return redirect(url_for('users.signup'))

    return render_template('admin/acc_req.html', form=form)
