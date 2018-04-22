#!/usr/bin/python3
import os
from flask import (Blueprint, Flask, jsonify, render_template)

app = Flask(__name__)

file_dir = os.path.abspath(os.path.dirname('__file__'))
print(file_dir)

def read_file(filename):
    file_handle = open(filename)
    file_info = file_handle.read()
    file_handle.close()
    return file_info

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    file_path = os.path.join(file_dir, 'api/v1/text/about_us/about_us.txt')
    about_us_doc = read_file(file_path)
    return render_template("about.html", about_us_doc=about_us_doc)

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/streams')
def streams():
    return render_template("streams.html")

@app.route('/join')
def join():
    return render_template("streams.html")

@app.route('/fflogs')
def fflogs():
    return render_template("scumbagdps.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
