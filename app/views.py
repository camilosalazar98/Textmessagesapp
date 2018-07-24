from app import app
from flask import render_template, session, redirect, url_for, session, flash,request
from twilio.rest import Client
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import views
from forms import Addform,Delform


################################################################


basedir = os.path.abspath(os.path.dirname(__file__))



app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLAlCHEMY_Track_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app ,db)
##########################################################
##########################################################
#Database basestuff
class phone_num(db.Model):
    __tablename__ = 'phone_numbers' #name of the talbe

    id = db.Column(db.Integer,primary_key = True) # id the inputs in the db
    name = db.Column(db.Text)#name of the students
    phone_number = db.Column(db.Integer)#The numbers to text


    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number} "




#################################################################
################################################################


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/message_func')
def message_func():
    #Your Account Sid and Auth Token from twilio.com/console
    account_sid = 
    auth_token =
    phone_num = request.args.get('phone_num')
    message_= request.args.get('message_')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body = message_,
                              from_='+13476948587',
                              to='+1'+phone_num)
    return render_template('home.html')
