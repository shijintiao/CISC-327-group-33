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
    #0 stands for buyers, 1 stands for sellers
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
    
class Banking_info(db.Model):
    #basic attributes
    id = db.Column(db.Integer, primary_key=True)
    Banking_name = db.Column(db.String(20),unique=False, nullable=True)
    Banking_account = db.Column(db.Integer, unique=True)
    #Banking token is a secret key from bank to customer so the customer won't need Personal identity verification to complete the transcation. 
    Banking_token = db.Column(db.String(80), unique=True,nullable=True)
    
    def __repr__(self):
        return '<Customer Bank %r)' % self.Banking_name
    
    
    
    
    
