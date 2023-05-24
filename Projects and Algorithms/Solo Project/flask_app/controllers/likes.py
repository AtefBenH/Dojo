from flask_app import app
from flask import render_template, redirect, request, session, jsonify
from flask_app.models.like import Like


@app.route('/likes/<int:book_id>/create')
def add_like(book_id):
    if 'user_id' in session:
        data = {
            'user_id' : session['user_id'],
            'book_id' : book_id
        }
        Like.save(data)
        return jsonify({'message' : "success"})
    return redirect('/')
