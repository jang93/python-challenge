
import io
import requests
import zipfile
import shutil
import re
from PIL import Image, ImageFilter

# response = requests.get(f'http://www.pythonchallenge.com/pc/def/oxygen.png', stream=True)
# with open('level-7.png', 'wb') as out_file:
#     shutil.copyfileobj(response.raw, out_file)
# del response

with open('level-7.png', 'rb') as in_file:
    im = Image.open(in_file)
    print(im.width)
    print(im.height)
    print(im.getpixel((0,0)))
    row = [im.getpixel((x, im.height/2)) for x in range(im.width)]
    row = row[::7]
    ords = [r for r, g, b, a in row if r == g == b]
    text = "".join(map(chr, ords))

    print("".join(map(chr, map(int, re.findall(r'\d+', text)))))
