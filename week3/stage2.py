import requests
from bs4 import BeautifulSoup

req = requests.get('http://tv.naver.com/r')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')

infos = html.select('div.cds')

# clip1 = infos[0]
#
# print(clip1.select_one('tooltip').text)
# print(clip1.select_one('dd.chn > a').text)
# print(clip1.select_one('span.hit').text)
# print(clip1.select_one('span.like').text)

for info in infos:
    title = info.select_one('tooltip').text
    chn = info.select_one('dd.chn > a').text
    hit = info.select_one('span.hit').text
    like = info.select_one('span.like').text

    print(chn, '/', title, '/', hit, '/', like)
