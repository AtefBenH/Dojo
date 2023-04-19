from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!' -- Instead of returning a simple string, we are returning a html file
    return render_template("index.html")

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<string:name>')
def say(name):
    #! ---------- 1st Method ---------
    if any(char.isdigit() for char in name) :
        return "You Should Give a Valid Name"
    return f'Hi {name}'
    #! ---------- 2nd Method ---------
    # for char in name :
    #     if char.isdigit() :
    #         return "You Should Give a Valid Name"
    # return f'Hi {name}'

@app.route('/repeat/<int:times>/<name>')
def repeat(times, name):
    return render_template("hello.html", times=times, name=name)
        

#Catches any route other than the ones specified
@app.errorhandler(404) 
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)

