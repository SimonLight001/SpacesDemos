import requests

JSON = {'users': 20}

r = requests.post('http://192.168.128.146/', json=JSON)
print(r.text)
