from flask import Flask, render_template, request
from random import *

app = Flask(__name__)

@app.route('/')
def index():
    number = randint(1, 100)
    print (number)
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(debug=True)