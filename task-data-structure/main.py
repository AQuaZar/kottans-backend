import requests
import json

url = "http://localhost:8000/"

for i in range(1, 6):
    data = {"data_type": "stack", "action": "push", "value": str(i)}
    data = json.dumps(data)
    r = requests.put(url, data=data)
for i in range(1, 3):
    data = {"data_type": "stack", "action": "pop"}
    data = json.dumps(data)
    r = requests.put(url, data=data)
    print(r.content)
