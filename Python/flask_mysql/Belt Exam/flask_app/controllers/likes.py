from flask_app import app
from flask import  redirect, session
from flask_app.models.like import Like

@app.route('/likes/<int:show_id>/create')
def create(show_id):
    if 'user_id' in session:
        data = {
            'user_id' : session['user_id'],
            'show_id' : show_id
        }
        Like.create(data)
        return redirect('/dashboard')
    return redirect('/')

@app.route('/likes/<int:show_id>/delete')
def delete(show_id):
    if 'user_id' in session:
        data = {
            'user_id' : session['user_id'],
            'show_id' : show_id
        }
        Like.unlike(data)
        return redirect('/dashboard')
    return redirect('/')
