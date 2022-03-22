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
        # print(input_json['image'])
        g = open("out.jpg", "wb")
        g.write(b64decode(input_json['image']))
        g.close()

        # s = json.loads(b64decode(input_json['image']))
        # print(s)
        im = Image.open(io.BytesIO('out.jpg'))
        print(im.size)
        return jsonify({
            "task":"done"
        })
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000
    )