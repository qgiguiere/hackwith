import os, json
from flask import Flask
from flask import render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/recon')
def recon():
    return render_template("recon.html")

@app.route('/categories')
def categories():
    return render_template("categories.html")

@app.route('/reversing')
def reversing():
    return render_template("reversing.html")

@app.route('/osint')
def osint():
    return render_template("osint.html")

@app.route('/mobile')
def mobile():
    return render_template("mobile.html")

@app.route('/wireless')
def wireless():
    return render_template("wireless.html")

@app.route('/phish')
def phish():
    return render_template("phish.html")

@app.route('/fuzzing')
def fuzzing():
    return render_template("fuzzing.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
