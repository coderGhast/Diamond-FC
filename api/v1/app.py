#!/usr/bin/python3

from flask import (Blueprint, Flask, jsonify, render_template)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/streams')
def streams():
    return render_template("streams.html")

@app.route('/join')
def join():
    return render_template("streams.html")

@app.route('/logs')
def join():
    return render_template("scumbagdps.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
