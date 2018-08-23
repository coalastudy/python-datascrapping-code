import requests
from bs4 import BeautifulSoup


raw = requests.get('https://tv.naver.com/r/').text
html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')
chn_infos = {}

for info in infos:
    chn = info.select_one('dd.chn > a').text
    chn_infos[chn] = {'hit': 0, 'like': 0}

for info in infos:
    chn = info.select_one('dd.chn > a').text
    hit = int(info.select_one('span.hit').text[4:].replace(',', ''))
    like = int(info.select_one('span.like').text[5:].replace(',', ''))

    chn_infos[chn]['like'] += like
    chn_infos[chn]['hit'] += hit

print(chn_infos)
