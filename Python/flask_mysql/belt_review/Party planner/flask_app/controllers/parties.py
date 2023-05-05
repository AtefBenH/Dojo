from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.party import Party
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_parties = Party.get_all()
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", all_parties = all_parties, user = logged_user)

@app.route('/parties/new')
def new_party():
    return render_template('new_party.html')

@app.route('/my_parties')
def show_parties():
    all_parties = Party.get_parties_by_user({'user_id' : session['user_id']})
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template('my_parties.html', all_parties = all_parties, user = logged_user)

@app.route('/parties/create', methods = ['POST'])
def create_party():
    if not Party.validate(request.form):
        return redirect('/parties/new')
    data = {
        **request.form, 'user_id' : session['user_id']
    }
    Party.create(data)
    return redirect ('/my_parties')

@app.route('/parties/<int:party_id>')
def show_party(party_id):
    party = Party.get_by_id({'id' : party_id})
    creator = User.get_by_id({'id' : party.user_id})
    return render_template('show_party.html', party = party, user = creator)

@app.route('/parties/<int:party_id>/edit')
def edit_party(party_id):
    party = Party.get_by_id({'id' : party_id})
    # creator = User.get_by_id({'id' : party.user_id})
    return render_template('edit_party.html', party = party)

@app.route('/parties/<int:party_id>/update', methods = ['POST'])
def update_party(party_id):

    if not Party.validate(request.form):
        return redirect(f'/parties/{party_id}/edit')
    data = {
        **request.form, 'user_id' : session['user_id'], 'id' : party_id
    }
    Party.update(data)
    return redirect ('/my_parties')

@app.route('/parties/<int:party_id>/delete')
def delete_party(party_id):
    Party.delete({'id' : party_id})
    return redirect('/my_parties')
