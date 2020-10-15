
import re
import requests
import pickle
import shutil
from pprint import pprint

response = requests.get(f'http://www.pythonchallenge.com/pc/def/banner.p', stream=True)
data = pickle.loads(response.content)
for line in data:
    print(''.join(k * v for k, v in line))
