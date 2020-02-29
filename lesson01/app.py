from flask import Flask
app = Flask(__name__)

# localhost:5000/
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # app.run()
    # app.run(port=3000) # specify port number
    app.run(debug=True) # activate debug mode (development environment)
