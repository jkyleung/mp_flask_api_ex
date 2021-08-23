import urllib.request, json

import requests

'''
33-joints
'landmark_id': int
'x': float
'y': float
'z': float
'visibility': float
'''

def get_json(method = 1, url="http://127.0.0.1:5000/api/v1/pose/tf"):
    if method == 1:
        # call with urllib
        with urllib.request.urlopen(url) as url_:
            data = json.loads(url_.read().decode())
            # print(data)
            print(data[1]['x'])
    elif method == 2:
        # call with requests
        r = requests.get(url)
        data = r.json()
        # print(data)
        print(data[1]['x'])

    elif method == 3:
        url = 'http://127.0.0.1:5000/stream/generate'
        i = int(input("i: "))
        # call with requests POST
        r = requests.post(url, json = {'i': i})
        data = r.json()
        print(data)
        for j in range(i):
            r = requests.post(url, json = {'i': j})
            data = r.json()
            print(data)

if __name__ == '__main__':
    method = input('Method: ')
    get_json(int(method))
    # get_json(int(method), 'http://ec2-13-250-24-24.ap-southeast-1.compute.amazonaws.com:8000/api/v1/pose/tf')