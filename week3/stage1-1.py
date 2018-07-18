import requests
from bs4 import BeautifulSoup


req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')

for info in infos:
    title = info.select_one('dt.title tooltip').text
    chn = info.select_one('dd.chn > a').text
    hit = info.select_one('span.hit').text[4:].replace(',', '')
    like = info.select_one('span.like').text[5:].replace(',', '')

    print(chn, '/', title, '/', hit, '/', like)
