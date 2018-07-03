import requests
from bs4 import BeautifulSoup

req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('div.cds')

print(infos[0].select('dt.title tooltip')[0].text, '/', infos[0].select('dd.chn > a')[0].text, '/', infos[0].select('span.hit')[0].text)
print(infos[1].select('dt.title tooltip')[0].text, '/', infos[1].select('dd.chn > a')[0].text, '/', infos[1].select('span.hit')[0].text)
print(infos[2].select('dt.title tooltip')[0].text, '/', infos[2].select('dd.chn > a')[0].text, '/', infos[2].select('span.hit')[0].text)
print(infos[3].select('dt.title tooltip')[0].text, '/', infos[3].select('dd.chn > a')[0].text, '/', infos[3].select('span.hit')[0].text)
print(infos[4].select('dt.title tooltip')[0].text, '/', infos[4].select('dd.chn > a')[0].text, '/', infos[4].select('span.hit')[0].text)
