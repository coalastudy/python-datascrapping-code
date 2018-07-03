
# requests library

import requests

req = requests.get('https://tv.naver.com/r/')

raw = req.text

print(raw)


# Array

subjects = ["데이터 수집", "웹개발", "파이썬"]

print(subjects[0])
print(subjects[1])
print(subjects[2])
