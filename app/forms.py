from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

app.config['SECRET_KEY'] = 'reherhwhwehreg~~!~!@@___DEZZZ_NUTS____$@!%RGREHREH#%355324131'
#Normally a environment variable but for learn purpose leave it as a string

class Addform(FlaskForm):
    name = StringField("Name of person")
    Phone_number_ = IntegerField("What is there phone number?")
    submit = SubmitField("Click to add")


class Delform(FlaskForm):
    id = IntegerField("Enter person id to remove: ")
    submit = SubmitField("Click to remove")
