from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    #basic attributes
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passord = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Integer, unique=True)
    bORs= db.Column(db.Integer, nullable=False)
    products = db.relationship("Product")

    def __repr__(self):
        return '<User %r>' % self.username

#Create Product class
class Product(db.Model):
    #basic attributes
    id = db.Column(db.Integer, primary_key=Ture)
    productName = db.Column(db.String(80), unique=True, nullable=False)
    seller = db.Column(db.Integer, db.ForeignKey("user_id"))
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Product %r)' % self.productName



# Create Transaction class
class Transaction(db.Model):
    # basic attributes
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    order_status = db.Column(db.String(80), unique=True, nullable=False)
    complete_time = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<User %r>' % self.name


# Create Transaction detail class
class Transaction_detail(db.Model):
    # basic attributes
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name