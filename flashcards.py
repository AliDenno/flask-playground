from flask import Flask, render_template
from datetime import datetime
from datareader import db

app = Flask(__name__)
counter = 0


@app.route("/")
def welcome_template():
    return render_template("welcome.html",
                           message="Wassssssaaaaap!!!"
                           )

@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html",
                           card=card
                           )

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
