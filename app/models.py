from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


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
