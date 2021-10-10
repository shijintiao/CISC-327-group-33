from qbay import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Identity


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

    def __repr__(self):
        return '<User %r>' % self.username


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


# This is the Product class
class Product(db.Model):
    # It is a self-increment attribute.
    # Every time implement an object,
    # it will be assigned an ID automatically
    id_incremental = db.Column(
        db.Integer,
        Identity(start=1, cycle=True),
        nullable=False, unique=True,
        primary_key=True)
    title = db.Column(
        db.String(50), nullable=False)
    description = db.Column(
        db.String(200), nullable=True)
    price = db.Column(
        db.String(5), nullable=False)
    last_modified_date = db.Column(
        db.String(20), nullable=False)
    owner_email = db.Column(
        db.String(50), nullable=False)


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
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    # create a new user
    user = User(username=name, email=email, password=password)
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
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]
