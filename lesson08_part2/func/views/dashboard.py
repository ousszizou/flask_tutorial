from flask import render_template, Blueprint

dash = Blueprint('dashboard', __name__)

@dash.route('/')
def home():
    return render_template('dashboard/admin.html')

@dash.route('/user')
def user():
    return '<h1> user - page </h1>'
