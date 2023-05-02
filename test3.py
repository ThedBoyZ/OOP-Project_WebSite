import requests
import json
new_data = "Ping"
#r = requests.get("http://127.0.0.1:8000/data")
r = requests.post("http://127.0.0.1:8000/user_data", data=json.dumps(new_data))

print(r)
print(r.json())