import requests
from bs4 import BeautifulSoup


req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')

dict = {}

for info in infos:
    chn = info.select('dd.chn > a')[0].text.strip()

    dict[chn] = {'hit': 0, 'like': 0}


for info in infos:
    chn = info.select('dd.chn')[0].text.strip()
    hit = int(info.select('span.hit')[0].text[4:].replace(',', ''))
    like = int(info.select('span.like')[0].text[5:].replace(',', ''))

    dict[chn]['hit'] += hit
    dict[chn]['like'] += like

print(dict)

channels = ['인형의 집', 'B조', '수미네 반찬', '복면가왕', '김비서가 왜그럴까']
hits = [25803, 280183, 12922, 8976, 801932]
likes = [80, 697, 61, 41, 13360]

meta = [{'hit': 25803, 'like': 80}, {'hit': 280183, 'like': 697}, {'hit': 12922, 'like': 61}, {'hit': 8976, 'like': 41}, {'hit': 801932, 'like': 13360}]