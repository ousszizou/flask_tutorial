from flask import render_template, Blueprint

dash = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static', url_prefix='/admin', static_url_path='/static')

@dash.route('/')
def home():
    return render_template('admin.html')

@dash.route('/user')
def user():
    return '<h1> user div structure </h1>'
