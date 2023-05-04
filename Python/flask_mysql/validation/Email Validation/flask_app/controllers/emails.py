from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route('/')
def index():
    return redirect('/emails/new')

@app.route('/emails/new')
def new_email():
    return render_template('index.html')

@app.route('/emails/create', methods = ['POST'])
def create_email():
    if Email.validate(request.form):
        session['email'] = request.form['email']
        Email.add(request.form)
        return redirect('/emails/success')
    return redirect('/')

@app.route('/emails/success')
def success():
    return render_template('success.html', emails = Email.get_all())

@app.route('/emails/<int:email_id>/destroy')
def destroy(email_id):
    Email.delete_by_id({'id' : email_id})
    return redirect('/emails/success')
