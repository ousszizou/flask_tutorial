from flask import Flask, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

@app.route('/')
def index():
    return 'index page'

@app.route('/visits-counter')
def visits():
    if 'visitor' in session:
        session['visitor'] = session.get('visitor') + 1
    else:
        session['visitor'] = 1
    return 'total visits : {}'.format(session.get('visitor'))

@app.route('/delete-session')
def delete():
    session.pop('visitor', None)
    return 'deleted...'
