import requests
import json

data = requests.get("https://api.covid19api.com/summary").json()
print(data)