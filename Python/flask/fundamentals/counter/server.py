from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'LiLy2018*'

@app.route('/')
def index() :
    session['count'] = 1
    return render_template("index.html")


if __name__ == "__main__" :
    app.run(debug=True)