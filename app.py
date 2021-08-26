import flask
from flask import request, jsonify
import sqlite3
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<p>home page</p>"

@app.route('/api/v1/motion/', methods=['GET', 'POST'])
def motion():
    if request.method == 'GET':
        # do not use GET method to call this api
        return "<p>This is the API of motion detection</p>"
    if request.method == 'POST':
        # require 33-joints landmark and return a score
        # in debug mode, score = sum(landmark[x])
        DEBUG_MODE = True
        
        if DEBUG_MODE:
            request_json = request.get_json()
            # structure: landmark[0:33]['id','x','y','z','visibility']
            score = 0
            for i in range(len(request_json)):
                score += request_json[i]['x']
            result = [{
                'score': score
            }]
            return jsonify(result)
        else:
            # request_json = request.get_json()
            return "POST request "

if __name__ == '__main__':
    app.run()