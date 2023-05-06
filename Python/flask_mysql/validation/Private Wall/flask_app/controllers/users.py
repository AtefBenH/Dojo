from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
import datetime

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id':session['user_id']})
    all_users = User.get_except({'id' : logged_user.id})
    #Get Sent messages
    s_messages = Message.get_messages_by_sender({'id' : logged_user.id})
    #Get Received messages
    r_messages = Message.get_messages_for_receiver({'id' : logged_user.id})
    return render_template("wall.html", user = logged_user, users = all_users, msg_s = len(s_messages), msg_r = len(r_messages) , r_messages = r_messages)

@app.route('/login', methods = ['POST'])
def login():
    user_from_db = User.get_by_email({'email' : request.form['email']})
    if user_from_db :
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            flash("Invalid Email/Password","login")
            return redirect('/')
        else :
            session['user_id'] = user_from_db.id
            return redirect ('/dashboard')
    flash("Invalid Email/Password","login")
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/users/create', methods = ['POST'])
def create_user():
    if User.validate (request.form):
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
        data = {
                **request.form, 'password':hashed_password
            }
        session['user_id'] = User.create(data)
        return redirect('/dashboard')
    return redirect('/')


    
