from lms_app import app
from lms_app import db
if __name__ == '__main__':
    with app.app_context():  # Set up an application context before working with the database
        db.create_all()  # Create the tables

    app.run(debug=True)
