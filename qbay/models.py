from qbay import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Identity
import re


'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)
    # shipping address is initiliy setting to None
    shipping_address = db.Column(
        db.String(120))
    # postal code is initiliy setting to None
    postal_code = db.Column(
        db.String(20))
    # balance is initiliy setting to $100
    balance = db.Column(
        db.Integer(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def updateProfile(self, name, address, postalCode):
        '''
        Update user profile
            Parameter：
                name(string):       new user name
                address(string):    new address
                postalCode(string): new postal code
            Returns:
                return true if update sucess
        '''
        # check if username meets the length requirement
        if len(name) < 2 and len(name) > 20:
            return False
        # check if whitespace take place at the first
        # or the last at prefix or suffix
        if name[0] == " " or name[-1] == " ":
            return False
        # check if username has special character which is not allowed
        if not(re.search(r'\W', name) is None):
            return False
        # check if address is non-empty
        if len(address) == 0:
            return False
        # check if address is alphanumeric-only
        string = r"~!@#$%^&*()_+-*/<>,[].\/"
        for i in string:
            if i in address:
                return False
        # check if postal code length is valid
        if len(postalCode) != 6:
            return False
        # check if postal code characters are vaild
        if (not(postalCode[0].isupper()) or
                not(postalCode[2].isupper()) or
                not(postalCode[4].isupper())):
            return False
        if (not(postalCode[1].isdigit()) or
                not(postalCode[3].isdigit()) or
                not(postalCode[5].isdigit())):
            return False
        self.username = name
        self.shipping_address = address
        self.postal_code = postalCode
        return True


# This is the Transaction class
class Transaction(db.Model):
    # It is a self-increment attribute.
    # Every time implement an object,
    # it will be assigned an ID automatically
    id_incremental = db.Column(
        db.Integer,
        Identity(start=1, cycle=True),
        nullable=False, unique=True,
        primary_key=True)
    # User's email address.
    # It could be not unique since
    # a same user can have more than one transactions.
    user_email = db.Column(
        db.String(50), nullable=False)
    product_id = db.Column(
        db.String(50), nullable=False)
    price = db.Column(
        db.String(5), nullable=False)
    date = db.Column(
        db.String(20), nullable=False)

    def __repr__(self):
        return '<Transaction %r>' % self.username


# This is the Review class
class Review(db.Model):
    # It is a self-increment attribute.
    # Every time implement an object,
    # it will be assigned an ID automatically
    Id_incremental = db.Column(
        db.Integer,
        Identity(start=1, cycle=True),
        nullable=False, unique=True,
        primary_key=True)
    user_email = db.Column(
        db.String(50), nullable=False)
    score = db.Column(
        db.String(5), nullable=False)
    # User's review.
    # It could be empty since
    # same user do not leave any text review.
    review = db.Column(
        db.String(200), nullable=True)


# create all tables
db.create_all()


def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''
    # email regex in RFC 5322 official standard
    r = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False
    # check if email meets RFC 5322 standard
    if re.match(r, email) is None:
        return False
    # check if password complexity meets the length requirement
    if len(password) <= 6:
        return False
    # check if password complexity meets the lower case requirment
    if password.isupper() or password.islower():
        return False
    # check if password complexity meets the specail characeter requirement
    if re.search(r'\W', password) is None:
        return False
    # check if username meets the length requirement
    if len(name) < 2 and len(name) > 20:
        return False
    # check if whitespace take place at the first
    # or the last at prefix or suffix
    if name[0] == " " or name[-1] == " ":
        return False
    # check if username has special character which is not allowed
    if not(re.search(r'\W', name) is None):
        return False

    # create a new user
    user = User(username=name, email=email, password=password)
    # initialize the address and balance
    user.balance = 100
    user.postal_code = ""
    user.shipping_address = ""
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    # email regex in RFC 5322 official standard
    r = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    # check if email meets RFC 5322 standard
    if not(re.match(r, email)):
        return False
    # check if password complexity meets the length requirement
    if len(password) <= 6:
        return False
    # check if password complexity meets the lower case requirment
    if password.isupper() or password.islower():
        return False
    # check if password complexity meets the specail characeter requirement
    if re.search(r'\W', password) is None:
        return False

    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]
