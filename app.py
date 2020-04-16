import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

# Defining variables database and MongoDB url
app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

MONGO = PyMongo(app)



@app.route('/')
def hello():
    return 'check it owt'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
