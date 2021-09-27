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
    
