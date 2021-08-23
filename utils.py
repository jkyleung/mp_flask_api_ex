import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mp_holistic = mp.solutions.holistic

import pickle
import base64
import numpy as np
import json

POSE_DEBUG = 1

# dont use 'with'
pose = mp_pose.Pose(static_image_mode=True, model_complexity=0, min_detection_confidence=0.5)

def img2json(img):
    """Convert a Numpy array to JSON string"""
    imgdata = pickle.dumps(img)
    jstr = json.dumps({"image": base64.b64encode(imgdata).decode('ascii')})
    return jstr

def json2img(jstr):
    """Convert a JSON string back to a Numpy array"""
    load = json.loads(jstr)
    imgdata = base64.b64decode(load['image'])
    img = pickle.loads(imgdata)
    return img

def run_pose_est(mode = POSE_DEBUG, json_input={}):
    result = get_landmark(mode, json_input)
    return result

def get_landmark(mode = POSE_DEBUG, json_input={}):
    if(mode == POSE_DEBUG):
        file = 'sample_img/1.jpg'
        image = cv2.imread(file)
        print("loaded image")
        image_height, image_width, _ = image.shape
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # print(image.shape)
        results = pose.process(image)
        print("processed image")

        return results.pose_landmarks.landmark
    else:
        img = json2img(json_input)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        # need to handle "NoneType" for the case that no pose detected
        if not results.pose_landmarks:
            return []
        return results.pose_landmarks.landmark

if(__name__ == '__main__'):
    print(run_pose_est())