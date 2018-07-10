
# requests library

import requests

req = requests.get('https://tv.naver.com/r/')

raw = req.text

print(raw)
