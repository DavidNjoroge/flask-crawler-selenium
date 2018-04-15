#!/usr/bin/env python3.6

from flask import Flask,jsonify
from server import module

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)