from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    Dojo.save_dojo(request.form)
    return redirect('/display')

@app.route('/display')
def display():
    return render_template('display.html')




