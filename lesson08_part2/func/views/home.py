from flask import render_template, Blueprint

home = Blueprint('index', __name__)

@home.route('/')
def index():
    return render_template('home/index.html')
