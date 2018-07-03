import requests
from bs4 import BeautifulSoup


req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')

for info in infos:
    title = info.select('dt.title tooltip')[0].text
    chn = info.select('dd.chn > a')[0].text

    hit = info.select('span.hit')[0].text[4:].replace(',', '')
    like = info.select('span.like')[0].text[5:].replace(',', '')

    print(chn, '/', title, '/', hit, '/', like)
