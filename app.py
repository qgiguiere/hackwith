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

if __name__ == "__main__":
    app.run(host='0.0.0.0')