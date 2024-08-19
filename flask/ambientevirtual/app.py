from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template():
    return render_template("curriculo.html")

