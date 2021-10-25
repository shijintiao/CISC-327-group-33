from qbay import app
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
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
            print("Failed! Your length of username must >2 and <20.")
            return False
        # check if whitespace take place at the first
        # or the last at prefix or suffix
        if name[0] == " " or name[-1] == " ":
            print("Failed! Username can not start or end with whitespace.")
            return False
        # check if username has special character which is not allowed
        if not(re.search(r'\W', name) is None):
            print("Failed! Username has unallowed special characters.")
            return False
        # check if address is non-empty
        if len(address) == 0:
            print("Failed! The address can not be empty.")
            return False
        # check if address is alphanumeric-only
        string = r"~!@#$%^&*()_+-*/<>,[].\/"
        for i in string:
            if i in address:
                print("Failed! The address is not alphanumeric-only.")
                return False
        # check if postal code length is valid
        if len(postalCode) != 6:
            print("Failed! The postal length is invalid.")
            return False
        # check if postal code characters are vaild
        if (not(postalCode[0].isupper()) or
                not(postalCode[2].isupper()) or
                not(postalCode[4].isupper())):
            print("Failed! The postal characters is invalid.")
            return False
        if (not(postalCode[1].isdigit()) or
                not(postalCode[3].isdigit()) or
                not(postalCode[5].isdigit())):
            print("Failed! The postal characters is invalid")
            return False
        self.username = name
        self.shipping_address = address
        self.postal_code = postalCode
        return self


# This is the Transaction class
class Transaction(db.Model):
    # It is a self-increment attribute.
    # Every time implement an object,
    # it will be assigned an ID automatically
    id_incremental = db.Column(
        db.Integer, primary_key=True,
        autoincrement=True,
        nullable=False)
    # User's email address.
    # It could be not unique since
    # a same user can have more than one transactions.
    user_email = db.Column(
        db.String(50), nullable=False)
    product_id = db.Column(
        db.String(50), nullable=False)
    price = db.Column(
        db.Integer, nullable=False)
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
        db.Integer, primary_key=True,
        autoincrement=True,
        nullable=False)
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
        db.Integer, primary_key=True,
        autoincrement=True,
        nullable=False)
    title = db.Column(
        db.String(50), nullable=False)
    description = db.Column(
        db.String(200), nullable=True)
    price = db.Column(
        db.Integer, nullable=False)
    last_modified_date = db.Column(
        db.String(20), nullable=False)
    owner_email = db.Column(
        db.String(50), nullable=False)

    def updateProduct(self, title, description, price):
        '''
        Update product information
          Parameters:
            id_incremental (Integer):     product ID
            title (string):    product title
            description (string): product description
            price (string): product price
          Returns:
            True if product update succeeded otherwise False
        '''

        if (self.title.startswith(' ') or
                self.title.endswith(' ')):
            print("Failed! Title can not start or end with whitespace.")
            return None
        # Check the length of title.
        if len(self.title) > 80:
            print("Failed! The length of title is too long.")
            return None
        # Check the length of description.
        if (len(self.description) > 200 or
                len(self.description) < 20):
            print("Failed! The length of description must >20 and <200.")
            return None
        # Check if the description is longer than title
        if len(self.description) < len(self.title):
            print("Failed! The description must be longer than title.")
            return None
        # Check if the price is in the correct range.
        if not (self.price in range(10, 10001)):
            print("Failed! The Price has to be in range[10, 10000].")
            return None
        # Check if the price is marked higher.
        if price < self.price:
            print("Failed! Price can only increase.")
            return None
        if int(price) >= self.price:
            self.price = price
        self.title = title
        self.description = description
        self.last_modified_date = datetime.now()
        return self


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
        print("Failed! This emali has been already used.")
        return False
    # check if email meets RFC 5322 standard
    if re.match(r, email) is None:
        print("Failed! Your email format is incorrect.")
        return False
    # check if password complexity meets the length requirement
    if len(password) <= 6:
        print("Failed! Your password is too short.")
        return False
    # check if password complexity meets the lower case requirment
    if password.isupper() or password.islower():
        print("Failed! Your password must have both upper and lower letters.")
        return False
    # check if password complexity meets the specail characeter requirement
    if re.search(r'\W', password) is None:
        print("Failed! Your password must have specail characters.")
        return False
    # check if username meets the length requirement
    if len(name) < 2 and len(name) > 20:
        print("Failed! Your length of username must >2 and <20.")
        return False
    # check if whitespace take place at the first
    # or the last at prefix or suffix
    if name[0] == " " or name[-1] == " ":
        print("Failed! Username can not start or end with whitespace.")
        return False
    # check if username has special character which is not allowed
    if not(re.search(r'\W', name) is None):
        print("Failed! Username has special character which is not allowed.")
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

    return user


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
        print("Failed! Your email format is incorrect.")
        return False
    # check if password complexity meets the length requirement
    if len(password) <= 6:
        print("Failed! Your password is too short.")
        return False
    # check if password complexity meets the lower case requirment
    if password.isupper() or password.islower():
        print("Failed! Your password is too simple.")
        print("There must be both lower and upper letters")
        return False
    # check if password complexity meets the specail characeter requirement
    if re.search(r'\W', password) is None:
        print("Failed! Password must contains specail characeter.")
        return False

    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        print("Failed! The user does not exist.")
        return None
    return valids[0]


def create_product(title, description, last_modified_date, price, owner_email):
    '''
    Creat a product
      Parameters:
        title (string):    product title
        description (string): product description
        last_modified_date(date): last modified date
        owner_email(string): owner email
      Returns:
       True if the product has been created successfully.
    '''
    D1 = datetime(2021, 1, 2)
    D2 = datetime(2025, 1, 2)
    price = int(price)
    # Check if the title is in the right format
    if (title.startswith(' ') or
            title.endswith(' ')):
        print("Failed! Title can not start or end with whitespace.")
        return None
    pattern = r'[a-zA-Z\s]+'
    if re.match(pattern, title) is None:
        print("Failed! The title is not alphanumeric-only.")
        return None
    # Check the length of title.
    if len(title) > 80:
        print("Failed! The length of title is too long.")
        return None
    # Check the length of description.
    if (len(description) > 200 or
            len(description) < 20):
        print("Failed! The length of description must >20 and <200.")
        return None
    # Check if the description is longer than title
    if len(description) < len(title):
        print("Failed! The description must be longer than title.")
        return None
    # Check if the price is in the correct range.
    if (price not in range(10, 10001)):
        print("Failed! The Price has to be in range[10, 10000].")
        return None
    # Check if the date is correct.
    if (last_modified_date < D1 or
            last_modified_date > D2):
        print("Failed! The effective date is from 2021-01-02 to 2025-01-02.")
        return None
        # The email address can't be empty.
    if owner_email is None:
        print("Failed! The owner email can not be empty.")
        return None
    owner_existed = User.query.filter_by(email=owner_email).all()
    if (len(owner_existed) != 1 or
            (len(owner_email) == 0)):
        print("Failed! The owner of this product does not exist.")
        return None
    # different product can't have same title.
    title_existed = Product.query.filter_by(title=title).all()
    if len(title_existed) > 0:
        print("Failed! This title exist already.")
        return None

    # create a new product
    product = Product(
        title=title, description=description,
        owner_email=owner_email, price=price,
        last_modified_date=last_modified_date)
    # add it to the current database session
    db.session.add(product)
    # actually save the product object
    db.session.commit()
    return product
