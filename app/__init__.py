from flask import Flask

app = Flask(__name__)

from app import views
from models import phone_num
from forms import Addform,Delform
