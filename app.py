import os
import json
from flask import Flask, render_template, session, request, redirect
from flask import url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env
    import bcrypt

app = Flask(__name__)

# Defining variables database and MongoDB url
app.config["MONGO_DBNAME"] = os.getenv('MONGO_DBNAME')
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

# First page - index.html where user is asked to enter their email address
# to access their schedule


@app.route('/')
def index():
    if 'email' in session:
        return redirect(url_for('modules'))

    return render_template('home.html')


@app.route('/base')
def base():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'email': request.form['email']})

    if login_user:
        session['email'] = request.form['email']
        return redirect(url_for('modules'))

    flash('email address not found')
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email': request.form['email']})

        if existing_user is None:
            users.insert({'email': request.form['email']})
            session['email'] = request.form['email']
            return redirect(url_for('modules'))

        flash('email already exists in our system')
        return render_template('register.html')

    return render_template('register.html')


@app.route('/logout')
def logout():
    session['email'] = None
    return render_template('home.html')


@app.route('/modules')
def modules():
    email = session['email']
    topics = list(mongo.db.topics.find())
    return render_template("modules.html",
                           subjects=mongo.db.subjects.find({'email': session['email']}),
                           subjectList=mongo.db.subjects.find({'email': session['email']}),
                           topics=list(mongo.db.topics.find({'email': session['email']})))


@app.route('/add_subject', methods=['POST'])
def add_subject():
    mongo.db.subjects.insert(
        {'subject': request.form['subjects'], 'email': session['email']})
    return redirect(url_for('modules'))


@app.route('/add_topic', methods=['POST'])
def add_topic():
    mongo.db.topics.insert(
        {
            'topic': request.form['topic'],
            'subject': request.form['subject'],
            "complete": False,
            'email': session['email']})
    return redirect(url_for('modules'))


@app.route('/delete/<topics_id>')
def delete(topics_id):
    mongo.db.topics.remove({'_id': ObjectId(topics_id)})
    return redirect(url_for('modules'))


@app.route('/notes')
def notes():
    email = session['email']
    return render_template("notes.html", subjects=mongo.db.subjects.find(
        {'email': session['email']}),
        notes=mongo.db.notes.find({'email': session['email']}))


@app.route('/add_notes', methods=['POST'])
def add_notes():
    mongo.db.notes.insert(
        {
            'subject': request.form['subject'],
            'note': request.form['note'],
            'title': request.form['title'],
            'email': session['email']})
    return redirect(url_for('notes'))


@app.route('/delete_note/<note_id>')
def delete_notes(note_id):
    mongo.db.notes.remove({'_id': ObjectId(note_id)})
    return redirect(url_for('notes'))


@app.route('/edit_note/<note_id>')
def edit_notes(note_id):
    this_note = mongo.db.notes.find_one({"_id": ObjectId(note_id)})
    return render_template('editnote.html', note=this_note)


@app.route('/update_notes/<note_id>', methods=["POST"])
def update_notes(note_id):
    notes = mongo.db.notes
    notes.update({'_id': ObjectId(note_id)},
                 {
        'title': request.form.get('title'),
        'subject':request.form.get('subject'),
        'note': request.form.get('note'),
        'email': session['email'],
    })
    return redirect(url_for('notes'))


@app.route("/toggle/<topics_id>", methods=["POST"])
def toggle_complete(topics_id):
    topics = mongo.db.topics
    topic = topics.find_one({'_id': ObjectId(topics_id)})
    if topic['complete'] is False:
        topics.update_one(
            topic,
            {

                "$set": {
                    'complete': True,
                }
            })
    else:
        topics.update_one(
            topic,
            {

                "$set": {
                    'complete': False,
                }
            })

    return "Success"


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
