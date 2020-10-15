
import io
import requests
import zipfile
import shutil
import re

response = requests.get(f'http://www.pythonchallenge.com/pc/def/channel.zip')
zf = zipfile.ZipFile(io.BytesIO(response.content))

# print(zf.namelist())
# print(zf.comment)

comments = []
print(zf.open("readme.txt").readlines())
file_name = "90052.txt"
while True:
    file_output = zf.read(file_name).decode('utf-8')
    comments.append(zf.getinfo(file_name).comment.decode('utf-8'))
    print(file_output)
    text = re.findall(r'Next nothing is (\d+)', file_output)
    if not text:
        print('ERrro')
        break
    else:
        file_name = f"{text[0]}.txt"

print(''.join(comments))