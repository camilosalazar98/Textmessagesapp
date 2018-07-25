from flask import Flask

app = Flask(__name__)

from app import views
from forms import Addform,Delform
from models import phone_num
