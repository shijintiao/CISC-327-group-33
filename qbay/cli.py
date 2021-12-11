from datetime import datetime
from flask_sqlalchemy import BaseQuery

from sqlalchemy.orm import query
from qbay.models import *
import sys
sys.path.append("..")


def login_page():
    print('\n-----------------------------------------\n'
          'Please enter your email'
          'address and password here'
          '\n-----------------------------------------\n')
    email = input('Please input email:\n')
    password = input('Please input password:\n')
    res = login(email, password)
    return res


def regsiter_page():
    print('-------------------------------------------------'
          '------------------------------------\n'
          'Please read the follow requirements carefully!'
          '\n-------------------------------------------------'
          '------------------------------------\n'
          '1.Your email address must follow the '
          'RFC5322 standard.\n'
          '2.Your password length must longer than 6 digits.\n'
          '3.Your password must include both '
          'upper letter and lower letters.')
    name = input('Please input your name:\n')
    email = input('Please input email:\n')
    password = input('Please input password:')
    password_twice = input('Please input the password again:')
    if password != password_twice:
        print('\nFailed! Passwords do not match.\n')
        return False
    res = register(name, email, password)
    return res


def create_page(email):
    title = input("\nPlease enter a title.\n")
    description = input("Please enter a description for your product\n")
    price = input("Please enter the price\n")
    pro = create_product(title, description, datetime.now(), price, email)
    return pro


def update_profile(user):
    name = input("\nPlease enter a new name\n")
    address = input("Please enter a new address\n")
    postalCode = input("Please enter a new postal code\n")
    user = user.updateProfile(name, address, postalCode)
    return user


def update_product(user):
    product_list = Product.query.filter_by(owner_email=user.email).all()
    print('\n%d product found!\n' % len(product_list))
    print('Your on sale product(s) list:')
    for i in range(len(product_list)):
        print('ID:%d Title:%-10s Price:%d' % (product_list[i].id_incremental,
              product_list[i].title, product_list[i].price))
    product_input = input('\nSelect one you want to see details'
                          '(Starts from 1):'
                          '\nor Type 0 to go back to previous page')
    if not product_input.isnumeric():
        print('You should enter a number!')
        return
    elif product_input == 0:
        return
    else:
        product_number = int(product_input) - 1
        if product_number not in range(0, len(product_list)):
            print('The number entered is out of range!')
            return
    print(
        '\nID:%d\nTitle:%s\nPrice:%d\nDescription:%s\nLast modified Date:%s\n'
        % (product_list[i].id_incremental, product_list[i].title,
            product_list[i].price, product_list[i].description,
            product_list[i].last_modified_date))

    if product_list[product_number] is not None:
        choice = int(input('\nType 1 to update product title.\n'
                           'Type 2 to update product description.\n'
                           'Type 3 to update product price.\n'
                           'Type 4 to update all product parameters.\n'
                           'Type 5 to to go back to previous page'))
        if 1 > choice or choice > 5:
            print('The choice is not in the list, please try again!')
            return
        else:
            if choice == 5:
                return
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
    else:
        print("No result found by this email!")
        return


def checkProduct(user):
    print(Product.query.all())
    print("Now you own " + str(user.balance) + " balance.")
    num = input("Which item would you like to purchase? type the ID"
                " or press letter to back.\n")
    if num.isdigit():
        purchase(Product.query.get(int(num)), user)
    else:
        return


def purchase(product, user):
    if user.balance >= product.price:
        transact(product, user)
        print("Purchase success!")
        print("Please give the review.")
        writeReview(user, product)
        product.update_status(1)
        print("Now you left " + str(user.balance) + " balance.")
        return
    else:
        print("Not enough money")
        return


def transact(product, user):
    Transaction(product_id=product.id_incremental, price=product.price,
                date=datetime, buyer=user, seller=product.owner_email)
    return


def writeReview(user, product):
    rev = input()
    soc = input("Please give a score from 1 to 10\n")
    if soc.isdigit():
        if int(soc) <= 10 and int(soc) >= 1:
            Review(user_email=user.email, score=int(soc),
                   product_id=product.id_incremental, review=rev)
    else:
        print("Please enter valid input.")
        writeReview(user, product)
    return
