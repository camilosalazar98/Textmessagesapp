from app import app
from flask import render_template, session, redirect, url_for, session, flash,request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField)
from db_setup import db,phone_num

from twilio.rest import Client





from app import views
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
                              from_='+',
                              to='+1'+phone_num)
    return render_template('home.html')
