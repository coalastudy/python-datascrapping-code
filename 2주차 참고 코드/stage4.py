import requests
from bs4 import BeautifulSoup

req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('div.cds')

choo = infos[0]

chootitle = choo.select('dt.title tooltip')[0]

print('/', chootitle.text, '/')
