from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form.get('pass')
        if username == 'admin' and password == '123456':
            return 'welcome to dashboard'
        else:
            return 'invalid username/password'

    return render_template('login.html')
