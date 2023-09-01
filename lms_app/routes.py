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
        acc_status = 2

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
                acc_type=acc_type,
                acc_status=acc_status
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
        user_acc_appproved = User.query.filter_by(acc_status='2').first()
        user = User.query.filter_by(username=form.username.data).first()
        users_with_user_acc = User.query.filter_by(acc_type='U').all()
        if users_with_user_acc and user_acc_appproved:

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
        else:
            flash('Login Not Allowed')
            return redirect(url_for('login'))

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
# account request for admin
@app.route('/admin/acc-req', methods=['GET', 'POST'])
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
            return redirect(url_for('signup'))

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
            return redirect(url_for('login'))

        except Exception as e:
            # Handle any other exceptions that might occur during registration
            db.session.rollback()  # Rollback the transaction
            flash('An error occurred during Form Submition.')
            return redirect(url_for('signup'))

    return render_template('admin/acc_req.html', form=form)


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
        user_acc_appproved = User.query.filter_by(acc_status='1').first()

        if user_admin and user_admin_exists and user_acc_appproved:
            #  check hash
            if bcrypt.check_password_hash(user_admin.password, form.password.data):
                login_user(user_admin)
                flash('Login Successfull')
                return redirect(url_for('admin_home'))
            else:
                flash('Wrong username or password')
        else:
            flash('Wrong username or password or account not approved')

    return render_template('admin/login.html', form=form)

# admin logout


@app.route('/admin/admin-logout', methods=['POST', 'GET'])
def admin_logout():
    logout_user()
    flash('Logout successfull')
    return redirect(url_for('login'))


# admin user view@app.route('/admin/view-users', methods=['POST', 'GET'])
@app.route('/admin/view-users', methods=['POST', 'GET'])
@login_required
def admin_view_users():
    # Retrieve users with account type 'u' and account status '1'
    users = User.query.filter_by(acc_type='U').all()

    # Retrieve admins with account type 'a' and account status '1'
    # admins = User.query.filter_by(acc_type='a', acc_status=1).all()

    # Retrieve users with account status '2' (not approved accounts)
    # not_approved_acc = User.query.filter_by(acc_status=2).all()
    # users = User.query.order_by(User.id)

    return render_template('admin/view_users_home.html', users=users,  title='View Users')


@app.route('/admin/approved_admin', methods=['POST', 'GET'])
@login_required
def approved_admin():
    admins = User.query.filter_by(acc_status = '1' ,acc_type = 'A').all()
    return render_template('admin/view_approved_admin.html', users=admins)


@app.route('/admin/not_approved_admin', methods=['POST', 'GET'])
@login_required
def not_approved_admin():
    admins = User.query.filter_by(acc_type='A', acc_status='0').all()
    return render_template('admin/view_not_app_admin.html', users=admins)


@app.route('/admin/view-contact', methods=['POST', 'GET'])
@login_required
def admin_view_contact():
    contacts = Contact.query.order_by(Contact.id)
    return render_template('admin/view_contact.html', contact = contacts,title='View Contact')
