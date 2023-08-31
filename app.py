from flask import Flask, render_template, url_for

# forms
from forms.signup import RegisterForm
from forms.contact import ContactForm

app = Flask(__name__)
# secret key for csrf token
app.config['SECRET_KEY'] = "01abab01ea5929f69085bf52ff7521aa"


# User routes

# User home page
@app.route('/')
def client_home():
    return render_template('client/index.html')

# user registeration
@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    form = RegisterForm()
    return render_template('client/signup.html', form=form, title="Register Now")

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    form = ContactForm()
    return render_template('client/contact.html', form=form, title="Contact Us")


# Admin routes


@app.route('/admin')
def admin_home():
    return render_template('admin/index.html')

# Add your admin routes here


if __name__ == '__main__':
    app.run(debug=True)
