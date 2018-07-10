import requests
from bs4 import BeautifulSoup

req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('div.cds')

print(infos[0].select_one('dt.title tooltip').text, '/', infos[0].select_one('dd.chn > a').text, '/', infos[0].select_one('span.hit').text)
print(infos[1].select_one('dt.title tooltip').text, '/', infos[1].select_one('dd.chn > a').text, '/', infos[1].select_one('span.hit').text)
print(infos[2].select_one('dt.title tooltip').text, '/', infos[2].select_one('dd.chn > a').text, '/', infos[2].select_one('span.hit').text)
print(infos[3].select_one('dt.title tooltip').text, '/', infos[3].select_one('dd.chn > a').text, '/', infos[3].select_one('span.hit').text)
print(infos[4].select_one('dt.title tooltip').text, '/', infos[4].select_one('dd.chn > a').text, '/', infos[4].select_one('span.hit').text)
