from flask import Flask, render_template
from forms import MyForm

app = Flask(__name__)

app.config.from_object('config.config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit() :
        return '<h1> username: {}, password: {}'.format(form.name.data, form.password.data)
    return render_template('login.html', form=form)
