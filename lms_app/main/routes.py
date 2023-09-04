from flask import Blueprint, render_template, redirect, flash, url_for
from lms_app.main.forms import (ContactForm)
# from lms_app.models import (Contact)
from lms_app import db
main = Blueprint('main', __name__)

@main.route('/')
def global_home():
    return render_template('client/index.html')


# @main.route('/contact', methods=['POST', 'GET'])
# def contact():
#     form = ContactForm()
#     if form.validate_on_submit():
#         username = form.name.data
#         email = form.email.data
#         message = form.message.data
#         try:
#             contact = Contact(
#                 username=username,
#                 email=email,
#                 message=message,

#             )
#             db.session.add(contact)
#             db.session.commit()
#             flash('Thankyou for contacting Us!')
#             return redirect(url_for('main.contact'))

#         except Exception as e:
#             # Handle any other exceptions that might occur during registration
#             db.session.rollback()  # Rollback the transaction
#             flash('An error occurred during Form Submission.')
#             return redirect(url_for('main.contact'))

#     return render_template('client/contact.html', form=form)

