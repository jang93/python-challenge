
import io
import requests
import zipfile
import shutil
import re

response = requests.get(f'http://www.pythonchallenge.com/pc/def/channel.zip')
zf = zipfile.ZipFile(io.BytesIO(response.content))

# print(zf.namelist())

comments = []
print(zf.open("readme.txt").readlines())
file_name = "90052.txt"
while True:
    file_output = zf.read(file_name).decode('utf-8')
    comments.append(zf.getinfo(file_name).comment.decode('utf-8'))
    print(file_output)
    text = re.search(r'Next nothing is (\d+)', file_output)
    if text is None:
        print('ERrro')
        break
    else:
        file_name = f"{text.group(1)}.txt"

print(''.join(comments))