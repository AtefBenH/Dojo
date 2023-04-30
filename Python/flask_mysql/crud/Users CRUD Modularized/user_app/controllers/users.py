from user_app import app
from flask import render_template, redirect, request, session, flash
from user_app.models.user import User

@app.route('/')
def go_index():
    return redirect('/users')
#Read ALL
@app.route("/users")
def index():
    return render_template("index.html", users=User.get_all())

#New User Route
@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

#Create New User
@app.route('/users/create', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return redirect ('/users')

#Show one user
@app.route('/users/<int:user_id>')
def show_one(user_id):
    data = {'id': user_id}
    one_user = User.get_one(data)
    return render_template("one_user.html", user = one_user)

#View Form to Update a User
@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    data = {'id': user_id}
    user_to_edit = User.get_one(data)
    return render_template("edit_user.html", user = user_to_edit)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update(user_id):
    data = {
        'id':user_id, **request.form
    }
    User.update(data)
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/destroy')
def delete(user_id):
    data = {'id': user_id}
    User.delete(data)
    return redirect('/')