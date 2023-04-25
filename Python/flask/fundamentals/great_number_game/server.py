from flask import Flask, render_template, session, redirect, request
from random import *

app = Flask(__name__)
app.secret_key = 'NoSecretsOnGithub'

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    if "number" not in session:
        session['number'] = randint(1, 100)
    if 'winners' not in session:
        session['winners']=[]
    # Print Tests
    print(session['number'])
    # print(session['count'])
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    try:
        session['guess'] = int(request.form['guess'])
        session['count']+=1
    #If the guess isn't a valid number
    except ValueError :
        return redirect ('/')
    return redirect ('/')

@app.route('/reset', methods=['GET', 'POST'])
def reset_and_win():
    if request.method == 'POST':
        session['winners'].append((request.form['first_name'], request.form['last_name'], session['count']))
        #Print Tests
        # for winner in session['winners']:
        #     print(winner)

    #Save the list of winners befor clearing the session
    winners = session.get('winners')
    session.pop('winners', None)
    #clear the session
    session.clear()
    #restore the list of winners
    session['winners'] = winners
    return redirect('/')

@app.route('/winners')
def show_winners():
    return render_template('winners.html')

if __name__ == "__main__" :
    app.run(debug=True)