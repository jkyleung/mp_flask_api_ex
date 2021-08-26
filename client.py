
import requests

from utils import *

def get_json(method, url="http://127.0.0.1:5000/api/v1/motion/"):
    # === call with requests POST
    if method == 1:
        # static image
        pose_result = run_pose_est()
        json_input = []
        for i in range(len(pose_result)):
            json_input.append({
                'landmark_id': i,
                'x': pose_result[i].x,
                'y': pose_result[i].y,
                'z': pose_result[i].z,
                'visibility': pose_result[i].visibility
            })
        r = requests.post(url, json = json_input)
        data = r.json()
        print(data)
    elif method == 2:
        # open cv video
        data = 'not finished'
        print(data)
    else:
        print("Error: unknown method")

if __name__ == '__main__':
    method = int(input("Method (1: image, 2: video): "))
    get_json(method)