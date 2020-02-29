from flask import Flask
from home.views import home
from dashboard.views import dash
app = Flask(__name__, static_folder=None)

app.register_blueprint(home)
app.register_blueprint(dash)
