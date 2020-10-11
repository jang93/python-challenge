
import re
import requests


response = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
text = re.search(r'<!--(.*)-->', response.text, re.DOTALL).group(1)
result = ''.join(re.findall(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', text))
print(result)