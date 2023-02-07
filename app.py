from flask import Flask, render_template
from helper import pets

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/animals/<pet_type>")
def animals(pet_type):
    html = '<h1>List of pets</h1>'
    html += '<ul>'
    for pet in pets[pet_type]:
        html += '<li><a href=""' + str(pet) + '</li>'
    html += '<ul>'
    return html

@app.route("/pet/<pet_type>/<pet_id>")
def pet(pet_type, pet_id):
    pet = '<h1>' + pet_type[pet_id] + '</h1>'
    return pet['name']


app.run(host='0.0.0.0', port=5000, debug=True)