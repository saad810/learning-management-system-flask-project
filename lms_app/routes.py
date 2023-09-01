from flask import redirect, url_for, render_template, flash
from flask_login import LoginManager, login_required, login_user, logout_user
from lms_app import app, db
# forms import
from lms_app.forms import RegisterForm, LoginForm, ContactForm
# db modelsimport
from lms_app.models import User, Contact
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)
# login config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# global home route


@app.route('/')
def global_home():
    return render_template('client/index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password, 10)
        acc_type = "U"

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
                acc_type=acc_type
            )
            db.session.add(user)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for('login'))

        except Exception as e:
            # Handle any other exceptions that might occur during registration
            db.session.rollback()  # Rollback the transaction
            flash('An error occurred during registration.')
            return redirect(url_for('signup'))

    return render_template('client/signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # users_with_user_acc = User.query.filter_by(acc_type='U').all()
        # if users_with_user_acc:
        if user:
            #  check hash
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Login Successfull')
                return redirect(url_for('user_home'))
            else:
                flash('Wrong username or password')
        else:
            flash('Wrong username or password')
        # else:
        #     flash('Login Not Allowed')

    return render_template('client/login.html', form=form)

# logout route


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    flash('Logout successfull')
    return redirect(url_for('login'))


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        username = form.name.data
        email = form.email.data
        message = form.message.data
        try:
            contact = Contact(
                username=username,
                email=email,
                message=message,

            )
            db.session.add(contact)
            db.session.commit()
            flash('Thankyou for contacting Us!')
            return redirect(url_for('contact'))

        except Exception as e:
            # Handle any other exceptions that might occur during registration
            db.session.rollback()  # Rollback the transaction
            flash('An error occurred during Form Submission.')
            return redirect(url_for('contact'))

    return render_template('client/contact.html', form=form)


# user protected routes

@app.route('/user-dash')
@login_required
def user_home():
    return render_template('client/protected_client/index.html')


# admin routes
@app.route('/admin')
@login_required
def admin_home():
    return render_template('admin/index.html')


@app.route('/admin/login', methods=['POSt', 'GET'])
def admin_login():
    form = LoginForm()
    username = form.username.data
    if form.validate_on_submit():
        user_admin = User.query.filter_by(username=username).first()
        user_admin_exists = User.query.filter_by(acc_type='A').first()
        if user_admin and user_admin_exists:
            #  check hash
            if bcrypt.check_password_hash(user_admin.password, form.password.data):
                login_user(user_admin)
                flash('Login Successfull')
                return redirect(url_for('admin_home'))
            else:
                flash('Wrong username or password')
        else:
            flash('Wrong username or password')

    return render_template('admin/login.html', form = form)

# admin logout
@app.route('/admin-logout', methods=['POST', 'GET'])
def admin_logout():
    logout_user()
    flash('Logout successfull')
    return redirect(url_for('login'))
