from datetime import datetime
from flask_sqlalchemy import BaseQuery, _include_sqlalchemy

from sqlalchemy.orm import query
from qbay.models import *
import sys
sys.path.append('..')


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
    title = input('\nPlease enter a title.\n')
    description = input('Please enter a description for your product\n')
    price = input('Please enter the price\n')
    pro = create_product(title, description, datetime.now(), price, email)
    return pro


def update_profile(user):
    name = input('\nPlease enter a new name\n')
    address = input('Please enter a new address\n')
    postalCode = input('Please enter a new postal code\n'
                       '(For example, K7L2R7 is valid\n')
    user = user.updateProfile(name, address, postalCode)
    return user


def update_product(user):
    product_list = Product.query.filter(
        Product.owner_email == user.email, Product.status == 0).all()
    # id_list stores all products' id on sale by this user
    id_list = []
    if len(product_list) == 0:
        print('\nYou have no products on sale!')
        return
    print('\n%d product found!' % len(product_list))
    print('Your on sale product(s) list:')
    for i in range(len(product_list)):
        print(' ID:%d Title:%-10s Price:%d' % (product_list[i].id_incremental,
              product_list[i].title, product_list[i].price))
        id_list.append(product_list[i].id_incremental)
    product_input = input('\nPlease enter a product ID to show details,'
                          ' or any other input to go back:\n')
    # Check if user's input is valid
    if not product_input.isnumeric() or int(product_input) not in id_list:
        return
    else:
        product_id = int(product_input)
        traget_product = Product.query.filter_by(id_incremental=product_id)[0]
    print(
        '\nID:%d\nTitle:%s\nPrice:%d\nDescription:%s\nLast modified Date:%s\n'
        % (traget_product.id_incremental,
           traget_product.title,
           traget_product.price,
           traget_product.description,
           traget_product.last_modified_date))

    if traget_product is not None:
        choice = int(input('\nType 1 to update product title.\n'
                           'Type 2 to update product description.\n'
                           'Type 3 to update product price.\n'
                           'Type 4 to update all product parameters.\n'
                           'Type 5 to to go back to previous page:'))
        if 1 > choice or choice > 5:
            print('The choice is not in the list, please try again!')
            return
        else:
            if choice == 5:
                return
            if choice == 1:
                new_title = input('What is the new title?')
                traget_product.updateProduct(
                    new_title,
                    traget_product.description,
                    traget_product.price)
                return traget_product
            if choice == 2:
                new_description = input('What is the new description?')
                traget_product.updateProduct(
                    traget_product.title,
                    new_description,
                    traget_product.price)
                return traget_product
            if choice == 3:
                new_price = input('What is the new price?')
                traget_product.updateProduct(
                    traget_product.title,
                    traget_product.description,
                    new_price)
                return traget_product
            if choice == 4:
                new_title = input('What is the new title?')
                new_description = input('What is the new description?')
                new_price = input('What is the new price?')
                traget_product.updateProduct(
                    new_title, new_description, new_price)
                return traget_product
    else:
        print('No result found by this email!')
        return


def check_product(user):
    product_list = Product.query.filter(
        Product.owner_email != user.email, Product.status == 0).all()
    # id_list stores all products' id on sale by this user
    id_list = []
    if len(product_list) == 0:
        print('\nNo others on sale products found!')
        return
    else:
        print('\n%d on sale product found!' % len(product_list))
        print('Other\'s sale product(s) list:')
    for i in range(len(product_list)):
        print(' ID:%d Title:%-10s Price:%d' % (product_list[i].id_incremental,
              product_list[i].title, product_list[i].price))
        id_list.append(product_list[i].id_incremental)
    product_input = input('\nPlease enter a product ID to show details,'
                          ' or any other input to go back:\n')
    # Check if user's input is valid
    if not product_input.isnumeric() or int(product_input) not in id_list:
        return
    else:
        product_id = int(product_input)
        traget_product = Product.query.filter_by(id_incremental=product_id)[0]
        print(
            '\nID:%d\nTitle:%s\nPrice:%d\nDescription:%s \
            \nLast modified Date:%s\n'
            % (traget_product.id_incremental,
               traget_product.title,
               traget_product.price,
               traget_product.description,
               traget_product.last_modified_date))
        print('You have ' + str(user.balance) + ' balance right now.')
        num = input('Would you like to purchase this product?\n'
                    'Enter 1 to confirm, otherwise will go back:\n')
        if num == '1':
            purchase(traget_product, user)
        else:
            return


def purchase(product, user):
    if user.balance >= product.price:
        transact(product, user)
        print('Purchase success!')
        write_review(user, product)
        product.update_status(1)
        product.update_buyer(user.email)
        print('Now you left ' + str(user.balance) + ' balance.')
        return
    else:
        print('Not enough money!')
        return


def transact(product, user):
    if user.email != product.owner_email:
        create_transcation(
            user.email, product.owner_email,
            product.id_incremental,
            product.price, datetime.now())
        user.balance -= int(product.price)
        seller = User.query.filter_by(email=product.owner_email).all()[0]
        seller.balance += int(product.price)
        db.session.commit()
        return
    else:
        print('\nFailed!You can not buy product of yourself!\n')


def write_review(user, product):
    rev = input('Please give a review.\n')
    soc = input('Please give a score from 1 to 10\n')
    # If create review failed, then repeat unitl success
    while not create_review(user, soc, product, rev):
        rev = input('Please give a review.\n')
        soc = input('Please give a score from 1 to 10\n')
    return


def check_order(user):
    prod = Product.query.filter(Product.status == 1).all()
    buy = []
    sold = []
    # id_list stores all products' id
    # which are bought or sold by user
    id_list = []
    if prod:
        for i in range(len(prod)):
            if prod[i].owner_email == user.email:
                sold.append(prod[i])
                # Add this product id to id_list
                id_list.append(prod[i].id_incremental)
            elif prod[i].buyer == user.email:
                buy.append(prod[i])
                # Add this product id to id_list
                id_list.append(prod[i].id_incremental)
        if len(buy) + len(sold) == 0:
            print('\nYou did not buy or sold anything yet.')
            return
        if len(buy) == 0:
            print('\nYou did not buy anything yet.')
        else:
            print('\nThese are what you had bought:')
            for i in range(len(buy)):
                print(' ID:%s Title:%s Price:%d ' % (buy[i].id_incremental,
                      buy[i].title, buy[i].price))
        if len(sold) == 0:
            print('\nYou did not sell anything yet.')
        else:
            print('\nThese are what you had been sold:')
            for i in range(len(sold)):
                print(' ID:%s Title:%s Price:%d ' % (sold[i].id_incremental,
                      sold[i].title, sold[i].price))
        id = input('\nPlease enter product ID to show details,'
                   ' or any other input to go back:\n')
        if id.isdigit():
            if int(id) in id_list:
                traget_product = Product.query.filter_by(
                    id_incremental=int(id)).all()[0]
                print('Product information: ')
                print(' Product ID: ' + id)
                print(' Product title: ' + traget_product.title)
                print(' Product description: ' + traget_product.description)
                print(' Product price: ' + str(traget_product.price))
                print('Review information: ')
                rev = Review.query.filter_by(product_id=int(id)).all()[0]
                print(' Product buyer email: ' + rev.user_email)
                print(' Buyer\'s score: ' + str(rev.score))
                print(' Comment: ' + rev.review)
                print('Transcation information: ')
                trans = Transaction.query.filter_by(
                    product_id=int(id)).all()[0]
                print(' Product buyer: ' + trans.buyer)
                print(' Product seller: ' + trans.seller)
                print(' Transcation time: ' + trans.date)
    else:
        print('\nYou did not buy or sold anything yet.')
    return


def add_balance(user):
    num = input('Enter the balance you would like to add:')
    user.add_balance(num)
    db.session.commit()
    return
