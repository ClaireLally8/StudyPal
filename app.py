import os
from flask import Flask, render_template, url_for, session, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

# Defining variables database and MongoDB url
app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

# First page - index.html where user is asked to enter their email address to access their schedule
@app.route('/')
def index():
    if 'email' in session:
        return render_template('home.html')

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'email' : request.form['email']})

    if login_user:
            session['email'] = request.form['email']
            return render_template('home.html')

    return 'email address not found! Try signing up!'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email' : request.form['email']})

        if existing_user is None:
            users.insert({'email' : request.form['email']})
            session['email'] = request.form['email']
            return render_template('home.html')
        
        return 'That email already exists!'

    return render_template('register.html')

@app.route('/dates', methods =['POST', 'GET'])
def dates():
    if request.method == 'POST':
        dates = mongo.db.dates
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        dates.insert({'startDate' : startDate, 'endDate' : endDate})
        return render_template('home.html')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
