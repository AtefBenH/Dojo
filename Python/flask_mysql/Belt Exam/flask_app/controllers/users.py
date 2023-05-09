from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        redirect('/dashboard')
    return render_template('index.html')

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
