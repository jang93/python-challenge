
import re
import requests

response = requests.get(f'http://www.pythonchallenge.com/pc/def/peak.html')
print(response.text)
