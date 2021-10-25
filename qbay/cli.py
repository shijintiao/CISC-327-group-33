from qbay.models import login, register
import sys
sys.path.append("..")


def login_page():
    email = input('Please input email:')
    password = input('Please input password:')
    res = login(email, password)
    return res


def regsiter_page():
    name = input('Please input your name:')
    email = input('Please input email:')
    password = input('Please input password:')
    password_twice = input('Please input the password again:')
    if password != password_twice:
        print('Failed! Passwords do not match.')
        return False
    res = register(name, email, password)
    return res
