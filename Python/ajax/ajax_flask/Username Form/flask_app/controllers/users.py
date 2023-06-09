from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, request, redirect

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return jsonify(User.get_all_json())

@app.route('/users/<int:id>')
def byId(id):
    return jsonify(User.get_one_by_user_id({'id':id}))

@app.route('/create/user',methods=['POST'])
def create_user():
    return jsonify(User.save(request.form))



