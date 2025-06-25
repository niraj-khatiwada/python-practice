import requests
import json

rs = requests.get(
    "https://jsonplaceholder.typicode.com/users",
)

if rs.status_code == 200:
    _json = rs.json()
    print(json.dumps(_json, indent=3))
