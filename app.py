import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


APP = Flask(__name__)

# Defining variables database and MongoDB url
APP.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.getenv('MONGO_URI')

MONGO = PyMongo(APP)



@app.route('/')
def hello():
    return 'Study Pal Test'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
