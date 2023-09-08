# from database import DBconnector
from lms_app.utils.database import DBconnector

db = DBconnector()


def check_duplicate_username(username):
    query = f"SELECT username, COUNT(username) AS username FROM person WHERE username = '{username}' GROUP BY username"
    result = db.execute_NoCommit(query)
    # print(result)
    if result:
        if result[0][1] > 1:
            return True
        else:
            return False
    else:
        return 0


def check_duplicate_email(email):
    query = f"SELECT email, COUNT(email) AS email FROM person WHERE email = '{email}' GROUP BY email"
    result = db.execute_NoCommit(query)
    # print(result)
    if result:
        if result[0][1] > 1:
            return True
        else:
            return False
    else:
        return 0


def check_user(value):
    query = f"SELECT username FROM person WHERE username =  '{value}'"
    result = db.execute_NoCommit(query)
    # print(result)
    if result:
        return True
    else:
        return False

def get_course_id(title):
    query = f"SELECT course_no FROM person WHERE title =  '{title}'"
    result = db.execute_NoCommit(query)
    return result

def get_subjects():
    query = "select sub_name from subjects"
    result = db.execute_NoCommit(query)
    return result

# print(get_subjects())

# data = get_subjects()

# for item in data:
#     value = item[0]  # Access the value inside the tuple
#     print(value)