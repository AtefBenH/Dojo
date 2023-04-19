from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def const_boxes():
    return render_template("play.html", x=3, color="#9FC5F8")

@app.route("/play/<int:x>")
def var_boxes(x):
    return render_template("play.html", x=x, color = "#9FC5F8")

@app.route("/play/<int:x>/<color>")
def var_color_boxes(x, color):
    return render_template("play.html", x=x, color=color)



if __name__=="__main__":
    app.run(debug=True)