
## The simple case :

    # app.py
    # config.py
    # static/
    # templates/

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=app.config["PORT"], debug=app.config["DEBUG"])
