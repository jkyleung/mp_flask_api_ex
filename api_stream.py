import flask
from flask import request, jsonify
import sqlite3
import json

from time import sleep

import mediapipe as mp
mp_pose = mp.solutions.pose

# import utils
from utils import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<p>home page</p>"

@app.route('/stream/generate', methods=['GET', 'POST'])
def api_stream():

    if request.method == 'POST':
        request_json = request.get_json()
        print(request_json)
        # output = input * 7
        i = 0
        if 'i' in request_json:
            i = int(request_json['i'])
        else:
            return ''''error: no input parameter "i" '''
        i = i * 7
        output = jsonify({'output': i})
        return output
    else:   # GET
        input = 20
        query_parameters = request.args
        if query_parameters.get('i'):   # exist
            input = int(query_parameters.get('i'))

        def generate():
            sum = 0
            yield '<div id="i"></div>'
            for i in range(input+1):
                sleep(.5)
                sum += i
                # yield str(i) + '</br>'
                yield '''<script>
                    var element = document.getElementById("i");
                    element.innerHTML = ''' + str(i) + '''
                    </script>'''
            # yield str(sum)
            sleep(1)
            yield '''<script>
                var element = document.getElementById("i");
                element.innerHTML = "sum = " + ''' + str(sum) + '''
                </script>'''

        return app.response_class(generate())

@app.route('/stream/img', methods=['GET', 'POST'])
def api_stream_img():
    if request.method == 'POST':
        # call TF, compute the landmark, return in json format
        request_json = request.get_json()
        # print(request_json)
        pose_result = run_pose_est(0, request_json)
        output = ""
        for i in range(len(pose_result)):
            output = output + '{:.3f}'.format(pose_result[i].x) + ', ' + '{:.3f}'.format(pose_result[i].y) + ', ' + '{:.3f}'.format(pose_result[i].z) + '</br>'
        # return output

        results = []
        # may not need the landmark_id
        for i in range(len(pose_result)):
            results.append({
                'landmark_id': i,
                'x': pose_result[i].x,
                'y': pose_result[i].y,
                'z': pose_result[i].z,
                'visibility': pose_result[i].visibility
            })

        return jsonify(results)

    else:   # GET
        return 'GET request page'

@app.route('/stream/skeleton', methods=['GET', 'POST'])
def api_stream_skeleton():
    if request.method == 'POST':
        # get skeleton landmarks json and return somethings with json
        return 1
    else:   # GET
        return 'This is GET request page, please use POST request'

if __name__ == '__main__':
    app.run()