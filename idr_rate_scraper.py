import requests

def getRates(url):
  json_data = requests.get(url)
  
  return json_data.json().values()
