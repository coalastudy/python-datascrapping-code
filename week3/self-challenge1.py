import requests
from bs4 import BeautifulSoup


raw = requests.get('http://tech.kakao.com/').text
html = BeautifulSoup(raw, 'html.parser')

tags = html.select('a.tag')

for tag in tags:
    print(tag.text)


for page in range(2, 11):
    raw = requests.get('http://tech.kakao.com/page/' + str(page)).text
    html = BeautifulSoup(raw, 'html.parser')

    tags = html.select('a.tag')

    for tag in tags:
        print(tag.text)
