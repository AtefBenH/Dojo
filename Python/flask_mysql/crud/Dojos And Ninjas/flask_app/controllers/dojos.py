from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def new_all():
    return render_template('dojo.html', dojos = Dojo.get_all())

@app.route('/dojos/<int:dojo_id>')
def show_dojo_ninjas(dojo_id):
    data = {'id': dojo_id}
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("one_dojo.html", dojo = dojo)

@app.route('/dojos/create', methods=['POST'])
def add_dojo():
    Dojo.save(request.form)
    return redirect ('/dojos')
