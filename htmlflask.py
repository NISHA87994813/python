from flask import Flask, render_template

app = Flask(__name__)

@app.route("/get")
def getdata():
    return render_template("html1.html")