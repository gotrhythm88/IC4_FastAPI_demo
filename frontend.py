import requests, json

myapi = "http://127.0.0.1:8000/"
raw_data = requests.get(myapi)

api =json.loads(raw_data.content)

print(api)
