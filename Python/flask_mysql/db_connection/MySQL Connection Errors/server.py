from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

#Read ALL
@app.route("/users")
def index():
    users = User.get_all()
    return render_template("index.html", users=users)

#New User Route
@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

#Create New User
@app.route('/users/create', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return redirect ('/users')

if __name__ == "__main__":
    app.run(debug=True)