import requests
import os
from flask_app import app
from flask import render_template, jsonify, redirect, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/superhero/search', methods = ['POST'])
def search():
    r = requests.get(f"https://superheroapi.com/api/{os.environ.get('FLASK_APP_API_KEY')}/search/{request.form['superhero']}")
    return jsonify(r.json())

