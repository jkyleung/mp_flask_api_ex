import flask
from flask import request, jsonify
import sqlite3
import json

import mediapipe as mp
mp_pose = mp.solutions.pose

# import utils
from utils import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/', methods=['GET'])
def home():
    return "<p>home page</p>"

@app.route('/api/v1/pose/tf', methods=['GET'])
def api_pose():
    
    pose_result = run_pose_est()
    output = ""
    for i in range(len(pose_result)):
        output = output + '{:.3f}'.format(pose_result[i].x) + ', ' + '{:.3f}'.format(pose_result[i].y) + ', ' + '{:.3f}'.format(pose_result[i].z) + '</br>'
    # return output

    results = []
    for i in range(len(pose_result)):
        results.append({
            'landmark_id': i,
            'x': pose_result[i].x,
            'y': pose_result[i].y,
            'z': pose_result[i].z,
            'visibility': pose_result[i].visibility
        })

    return jsonify(results)

    '''
    pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
    image = cv2.imread('sample_img/1.jpg')
    image_hight, image_width, _ = image.shape
    pose_results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    return str(f'nose landmark: ('
        f'{pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width},'
        f'{pose_results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_hight})')
    '''

if __name__ == '__main__':
    app.run()