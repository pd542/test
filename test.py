import requests

import json

import base64

import os

url="https://gitee.com/google-ad/googlead/raw/master/ads/jisu/jisud"

r=requests.get(url)

origStr=r.text

missing_padding = 4 - len(origStr) % 4 

if missing_padding: 

    origStr += '=' * missing_padding

r=base64.b64decode(origStr)

r=json.loads(r)

results=""

for i in r:

    results=results+i["Linkserver"]+"\n"

print(results)

results=base64.b64encode(bytes(results,'utf-8'))

f=open('test.md','wb')

f.write(results)

f.close()
