from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField


class Addform(FlaskForm):
    name = StringField("Name of person")
    Phone_number_ = IntegerField("What is there phone number?")
    submit = SubmitField("Click to add")


class Delform(FlaskForm):
    id = IntegerField("Enter person id to remove: ")
    submit = SubmitField("Click to remove")
