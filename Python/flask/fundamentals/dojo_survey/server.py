from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'NoSecretsOnGithub'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    #Debug
    print(request.form)
    hobbies = []
    session['name'] = request.form['name']
    session['gender'] = request.form['gender']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if 'hobby1' in request.form :
        hobbies.append(request.form['hobby1'])
    if 'hobby2' in request.form :
        hobbies.append(request.form['hobby2'])
    if 'hobby3' in request.form :
        hobbies.append(request.form['hobby3'])
    if 'hobby4' in request.form :
        hobbies.append(request.form['hobby4'])
    if 'hobby5' in request.form :
        hobbies.append(request.form['hobby5'])
    if 'hobby6' in request.form :
        hobbies.append(request.form['hobby6'])

    session['hobbies'] = hobbies

    print(session['hobbies'], "*"*100)
    print(hobbies)
    return redirect('/display')

@app.route('/display')
def display():
    return render_template('display.html')




if __name__ == "__main__":
    app.run(debug=True)