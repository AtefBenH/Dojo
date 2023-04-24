from flask import Flask, render_template, session, redirect, request
from random import *

app = Flask(__name__)
app.secret_key = 'LiLy2018*'
winners = []


@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    if "number" not in session:
        session['number'] = randint(1, 100)
    print(session['number'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    try:
        session['count']+=1
        session['guess'] = int(request.form['guess'])
    except ValueError :
        return redirect ('/')
    return redirect ('/')

@app.route('/reset', methods=['POST'])
def reset_and_win():
    winners.append((request.form['first_name'], request.form['last_name'], session['count']))
    for winner in winners:
        print(winner)
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/winners')
def show_winners():
    return render_template('winners.html')

if __name__ == "__main__" :
    app.run(debug=True)