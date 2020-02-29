
## instance folder

    # config.py
    # run.py
    # instance/
    #   config.py
    # yourapp/
    #   __init__.py
    #   models.py
    #   views.py
    #   templates/
    #   static/

from flask import Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=app.config["PORT"], debug=app.config["DEBUG"])
