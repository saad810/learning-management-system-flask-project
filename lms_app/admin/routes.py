from flask import Blueprint, redirect, url_for, flash, render_template
from lms_app.users.forms import (LoginForm)
from flask_login import  login_required, login_user, logout_user
from lms_app.models import User, Contact
from lms_app import bcrypt

admin = Blueprint('admin', __name__)





@admin.route('/admin')
@login_required
def admin_home():
    return render_template('admin/index.html')


@admin.route('/admin/login', methods=['POSt', 'GET'])
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
                return redirect(url_for('admin.admin_home'))
            else:
                flash('Wrong username or password')
        else:
            flash('Wrong username or password or account not approved')

    return render_template('admin/login.html', form=form)

# admin logout


@admin.route('/admin/admin-logout', methods=['POST', 'GET'])
def admin_logout():
    logout_user()
    flash('Logout successfull')
    return redirect(url_for('admin.login'))


# admin user view@app.route('/admin/view-users', methods=['POST', 'GET'])
@admin.route('/admin/view-users', methods=['POST', 'GET'])
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


@admin.route('/admin/approved-admin', methods=['POST', 'GET'])
@login_required
def approved_admin():
    admins = User.query.filter_by(acc_status='1', acc_type='A').all()
    return render_template('admin/view_approved_admin.html', users=admins)


@admin.route('/admin/not-approved-admin', methods=['POST', 'GET'])
@login_required
def not_approved_admin():
    admins = User.query.filter_by(acc_type='A', acc_status='0').all()
    return render_template('admin/view_not_app_admin.html', users=admins)


@admin.route('/admin/view-contact', methods=['POST', 'GET'])
@login_required
def admin_view_contact():
    contacts = Contact.query.order_by(Contact.id)
    return render_template('admin/view_contact.html', contact=contacts, title='View Contact')


# create course
admin.route('/create-course')


@login_required
def admin_create_course():
    return render_template('admin\course\create_course.html')
