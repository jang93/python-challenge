
import re
import string
from string import ascii_lowercase

import requests

response = requests.get('http://www.pythonchallenge.com/pc/def/map.html')
text = re.findall(r'<font color="#f000f0">(.*?)</tr></td>', response.text, re.DOTALL)[-1]
translation = text.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:]+string.ascii_lowercase[:2])

print(text.translate(translation))
print('map'.translate(translation))