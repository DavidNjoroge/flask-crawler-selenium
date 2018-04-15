#!/usr/bin/env python3.6

from flask import Flask,jsonify
from server import request

app = Flask(__name__)

@app.route('/')
def index():
    data = request()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)