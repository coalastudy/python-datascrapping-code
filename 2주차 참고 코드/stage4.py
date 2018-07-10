import requests
from bs4 import BeautifulSoup

req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('div.cds')

first = infos[0]

first_title = first.select_one('dt.title tooltip')

print('/', first_title.text, '/')
