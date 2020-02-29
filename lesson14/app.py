from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/connect_to_mongo"

mongo = PyMongo(app)

@app.route('/add')
def add_user():
    user = mongo.db.users
    user.insert({'name': 'algorithm'})
    return 'added user..'
