import requests

url = "localhost:5000/keliamieji/1988"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)