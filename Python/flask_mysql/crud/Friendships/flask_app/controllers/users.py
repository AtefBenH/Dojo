from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/friendships')

@app.route('/friendships')
def friendships():
    users = User.get_all_users()
    friendships = User.get_all_friendships()
    # unfriends = User.get_user_non_friend({'id' : 1})
    # print('@'*30, friendships, '@'*30)
    return render_template('friendships.html', users = users, friendships = friendships)


@app.route('/users/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/friendships')

@app.route('/friendships/create', methods=['POST'])
def create_friendship():
    User.add_friendship(request.form)
    return redirect('/friendships')