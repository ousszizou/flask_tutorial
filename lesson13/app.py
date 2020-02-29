from flask import Flask , url_for , render_template, redirect, request, abort, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'algorithm secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    return render_template('dash.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            flash(message='welcome to dashboard, {}'.format(username))
            return redirect('dashboard')
        else:
            error = 'invalid username / password, please try again!'
            return render_template('login.html', error = error)
    else:
        return render_template('login.html')
