
# ‫‪run.py‬‬
# ‫‪config/‬‬
#     __init__.py‬‬‬
#  ‫‪default.py‬   ‬
# ‫‪production.py‬    ‬
#  ‫‪development.py‬   ‬
# ‫‪instance/‬‬
#     ‫‪config.py‬‬
# ‫‪yourapp/‬‬
# ‫‪  __init__.py‬‬
# ‫‪  models.py‬‬
# ‫‪  views.py‬‬
# ‫‪static/‬‬

from flask import Flask
app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')
# Load the configuration from the instance folder
app.config.from_pyfile('config.py')
# Load the file specified by the APP_CONFIG_FILE environment variable
app.config.from_envvar('APP_SETTINGS')

# export APP_SETTINGS=/path_of_file.py (linux & mac)
# set  APP_SETTINGS=/path_of_file.py (windows)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=app.config['PORT'])
