
import re
import requests

nothing = '63579'
while True:
    response = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}')
    print(response.text)
    text = re.findall(r'and the next nothing is (\d+)', response.text)[0]
    if text is None:
        print('ERrro')
        break
    else:
        nothing = text
    print(nothing)

