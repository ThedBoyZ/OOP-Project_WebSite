import requests
import json

search = {"depart": "BKK", "arrival": "CNX", "travelday": "Monday"}
r = requests.post("http://127.0.0.1:8000/search_flight", json=search)
print(r)
print(r.json())