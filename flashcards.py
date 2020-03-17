from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
counter = 0


@app.route("/")
def welcome_template():
    return render_template("welcome.html")


@app.route("/welcome")
def welcome():
    return "Welcome to my Flash Cards Application!"


@app.route("/date")
def date():
    return "This page is being served at " + str(datetime.now())


@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return "This page was served " + str(counter) + " times"
