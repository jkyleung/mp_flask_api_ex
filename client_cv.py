import requests
import cv2

from utils import img2json, json2img

def get_json(url = 'http://127.0.0.1:5000/stream/img'):
    # call with requests

    # === for static image ===
    '''
    frame = cv2.imread('1.jpg')
    json_img = img2json(frame)
    # img = json2img(json_img)

    # cv2.imshow('Img', img)
    # cv2.waitKey(0)
    # cv2.destoryAllWindows()
    
    r = requests.post(url, json = json_img)
    data = r.json()

    print(data[30])
    '''

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        json_img = img2json(image)
        
        r = requests.post(url, json = json_img)
        data = r.json()
        if data:
            print(data[30])

        cv2.imshow('Img', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
    

if __name__ == '__main__':
    get_json()
    # get_json('http://ec2-13-212-27-247.ap-southeast-1.compute.amazonaws.com:8000/stream/img')
