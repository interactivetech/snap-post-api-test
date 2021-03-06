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
        s = input_json['image']
        print(len(s))
        # print(input_json['image'])
        # arr = []
        # for i in range(len(s)):
        #     arr.append(s[i])
        g = open("out.txt", "w")
        g.write(input_json['image'])
        g.close()
        # g.write(decodebytes(bytes(input_json['image'].encode('utf-8'))))
        # g.close()

        # # s = json.loads(b64decode(input_json['image']))
        # # print(s)
        # im = Image.open('/home/ec2-user/snap-post-api-test/out.jpg')
        # print(im.size)
        return jsonify({
            "task":input_json['image']
        })
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000
    )