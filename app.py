import os
# Using Flask since Python doesn't have built-in session management
from flask import Flask, session, render_template, request, jsonify
# Our target library
import requests
import json
from pathlib import Path
from base64 import encodebytes, decodebytes, b64decode
from PIL import Image
import io
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to dalleapi.com"

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == "POST":
        input_json = request.get_json(force=True) 
        print(len(input_json['image']))
        s = json.loads(b64decode(input_json['image']).encode('utf-8'))
        print(s)
        # im = Image.open(io.BytesIO(s))
        # print(im.size)
        return jsonify({
            "task":"done"
        })
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000
    )