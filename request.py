import requests

URL = "http://127.0.0.1:8000/resources"

response = requests.get(url=URL)
print(response.json())