from flask import Flask
from views.home import home
from views.dashboard import dash

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(dash, url_prefix='/dash')
