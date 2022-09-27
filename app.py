import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/gratitude")
def gratitude():
    return render_template('/gratitude.html')


@app.route("/ideas")
def ideas():
    return render_template('/ideas.html')


@app.route("/goals")
def goals():
    return render_template('/goals.html')


@app.route("/journal")
def jounral():
    return render_template('/journal.html')
