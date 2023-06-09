from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas/new')
def new_ninja():
    return render_template('new_ninja.html', all_dojos= Dojo.get_all())

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f'/dojos/{dojo_id}')
