from datetime import date, datetime
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
    date = datetime.now()
    pro = create_product(title, description, date, price, email)
    return pro


def update_profile(user):
    name = input("Please enter a new name\n")
    address = input("Please enter a new address\n")
    postalCode = input("Please enter a new postal code\n")
    user = user.updateProfile(name, address, postalCode)
    return user


def update_product():
    product_email = input('Please enter the email address '
        'if you wnat to update a product.')
    product_number = int(input('What is the product number for'
        ' your product')) - 1
    product_list = Product.query.filter_by(owner_email=product_email).all()
    if product_list[product_number] is not None:
        choice = int(input('Type 1 to update product title.\n'
                       'Type 2 to update product description.\n'
                       'Type 3 to update product price.\n'
                       'Type 4 to update all product parameters.\n'))
        if 1 > choice or choice > 4:
            print('The choice is not in the list, please try again!')
            update_page()
        else:
            if choice == 1:
                new_title = input('What is the new title?')
                product_list[product_number].updateProduct(
                    new_title,
                    product_list[product_number].description,
                    product_list[product_number].price)
                return product_list[product_number]
            if choice == 2:
                new_description = input('What is the new description?')
                product_list[product_number].updateProduct(
                    product_list[product_number].title,
                    new_description,
                    product_list[product_number].price)
                return product_list[product_number]
            if choice == 3:
                new_price = input('What is the new price?')
                product_list[product_number].updateProduct(
                        product_list[product_number].title,
                        product_list[product_number].description,
                        new_price)
                return product_list[product_number]
            if choice == 4:
                new_title = input('What is the new title?')
                new_description = input('What is the new description?')
                new_price = input('What is the new price?')
                product_list[product_number].updateProduct(
                    new_title, new_description, new_price)
                return product_list[product_number]
