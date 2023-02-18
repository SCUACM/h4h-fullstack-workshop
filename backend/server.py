import requests
from flask_cors import CORS

from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

@app.route("/")
def get_api_call():
    response = requests.get('https://raw.githubusercontent.com/SCUACM/h4h-fullstack-workshop/main/data.json')

    return response.json()

@app.route("/dict")
def get_dictionary():
    dictionary = {
        "year": 2023, 
        "name": "Hack for Humanity 2023!", 
        "data": [1, 2, 3, 4, 5]
    }

    return jsonify(dictionary)