from app import app
from flask import render_template, session, redirect, url_for, session, flash,request
from twilio.rest import Client
import os
from flask import Flask
from app import views




@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'] )

#Get the name of the user and phone number

def Addusers():
    form = Addform()
    if form.validate_on_submit():
        name = form.name.data
        phone_number1 = form.phone_number.data
        new_user = phone_num(name,phone_number)
        db.session.add(name,phone_number1)
        db.session.commit()
        return redirect(url_for('list_users'))

    return render_template('add.html',form=form)


@app.route('/list')
def list_users():
    users = phone_num.query.all()
    return render_template('list.html',users = phone_num)

@app.route('/delete',methods = ['GET','POST'])
def del_user():
    form = Delform()
    if form.validate_on_submit():
        id = form.id.data
        users = phone_num.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('list_of_users'))

    return render_template('delete.html',form=form)

@app.route('/message_func')
def message_func():
    #Your Account Sid and Auth Token from twilio.com/console
    account_sid = ''
    auth_token = ''
    phone_num = request.args.get('phone_num')
    message_= request.args.get('message_')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body = message_,
                              from_='+13476948587',
                              to='+1'+phone_num)
    return render_template('home.html')
