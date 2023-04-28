from flask import Flask, render_template, redirect, request, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'NoSecrectOnGithub'

def process_farm():
    session['amount'] = random.randint(10, 20)
    session['gold']+= session['amount']
    session['activities'].append("<div class='text-success'>Earned " + str(session['amount']) + " from the Farm! (" + str(session['datetime']) + ")</div>")
    return redirect('/')

def process_cave():
    session['amount'] = random.randint(5, 10)
    session['gold']+= session['amount']
    session['activities'].append("<div class='text-success'>Earned " + str(session['amount']) + " from the Cave! (" + str(session['datetime']) + ")</div>")
    return redirect('/')

def process_house():
    session['amount'] = random.randint(2, 5)
    session['gold']+= session['amount']
    session['activities'].append("<div class='text-success'>Earned " + str(session['amount']) + " from the House! (" + str(session['datetime']) + ")</div>")
    return redirect('/')

def process_casino():
    session['amount'] = random.randint(-50, 50)
    session['gold']+= session['amount']
    if session['amount']>= 0 :
        session['activities'].append("<div class='text-success'>Entered a Casino and won " + str(session['amount']) + " Golds!!!! Yaaaah.. (" + str(session['datetime']) + ")</div>")
    else:
        session['activities'].append("<div class='text-danger'>Entered a Casino and lost " + str(session['amount']) + " Golds.... Outch.. (" + str(session['datetime']) + ")</div>")
    return redirect('/')

form_handlers = {
    'farm': process_farm,
    'cave': process_cave,
    'house': process_house,
    'casino': process_casino,
}

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold']=0
    if 'activities' not in session:
        session['activities'] = []
    if 'moves' not in session:
        session['moves'] = 0
    if 'datetime' not in session:
        session['datetime']=''
    if 'amount' not in session:
        session['amount'] = 0
    return render_template('index.html')

@app.route('/', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():
    if session['moves']<15 and session['gold']<500:
        session['moves']+=1
        session['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form_name = request.form.get('building')
        handler = form_handlers.get(form_name)
        if handler:
            return handler()
        else:
            return ('Unknown Form')



if __name__ == "__main__":
    app.run(debug=True)