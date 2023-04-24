from flask import Flask, render_template, session, redirect, request

#Decoding Cookies
# import base64
# cookie_val1 = "eyJjb3VudCI6NjAsImZha2VfY291bnQiOjUwfQ.ZEXHhA==="
# cookie_val2 = "4YrzGRZ4CYyJd9kP6gPJ2kTsFfQbCHqZ==="
# res1 =  base64.urlsafe_b64decode(cookie_val1)
# res2 =  base64.urlsafe_b64decode(cookie_val2)
# print(res1)
# print(res2)

app = Flask(__name__)
app.secret_key = 'LiLy2018*'

@app.route('/')
def index() :
    if "fake_count" not in session:
        session["fake_count"] = 0
    if "count" not in session:
        session["count"] = 1
    else:
        session['count'] += 1

    return render_template("index.html")
    
    # return render_template("index.html", res1=res1, res2=res2)

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_more', methods=['POST'])
def add_more():
    session['fake_count'] += int(request.form['num'])
    session['count'] += int(request.form['num'])-1
    return redirect('/')



if __name__ == "__main__" :
    app.run(debug=True)