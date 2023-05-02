from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/friendships')

@app.route('/friendships')
def friendships():
    friendships = User.get_all_friendships()
    print('@'*30, friendships, '@'*30)
    users = User.get_all_users()
    return render_template('friendships.html', users = users, friendships = friendships)

@app.route('/users/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/friendships')

@app.route('/friendships/create', methods=['POST'])
def create_friendship():
    User.add_friendship(request.form)
    return redirect('/friendships')