
import re
import collections
import requests


response = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
text = re.findall(r'<!--(.*?)-->', response.text, re.DOTALL)[-1]
char_dict = collections.Counter(text)
print(sorted(char_dict.keys(), key=char_dict.get))