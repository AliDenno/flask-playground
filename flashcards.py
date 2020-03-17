from flask import Flask
from datetime import datetime

app = Flask(__name__)
counter = 0


@app.route("/")
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
