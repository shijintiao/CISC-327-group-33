from datetime import date
from qbay.models import *
import sys
sys.path.append("..")


def login_page():
    email = input('Please input email:\n')
    password = input('Please input password:\n')
    res = login(email, password)
    return res


def regsiter_page():
    name = input('Please input your name:\n')
    email = input('Please input email:\n')
    password = input('Please input password:')
    password_twice = input('Please input the password again:\n')
    if password != password_twice:
        print('Failed! Passwords do not match.\n')
        return False
    res = register(name, email, password)
    return res


def create_page(email):
    title = input("Please enter a title.\n")
    description = input("Please enter a description for your product\n")
    price = input("Please enter the price\n")
    date = date.today()
    pro = create_product(title, description, date, price, email)
    return pro


def update_profile(user):
    name = input("Please eneter new name\n")
    address = input("Please enter new address\n")
    postalCode = input("Please enter new postal code\n")
    user = user.updateProfile(name, address, postalCode)
    return user