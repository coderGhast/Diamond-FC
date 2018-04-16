#!/usr/bin/python3

from flask import (Blueprint, Flask, jsonify, render_template)

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
