from flask import render_template , Blueprint

home = Blueprint('index', __name__, template_folder='templates', static_folder='static', static_url_path='/static')

@home.route('/')
def index():
    return render_template('index.html')
