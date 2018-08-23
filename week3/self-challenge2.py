import requests
from bs4 import BeautifulSoup


raw = requests.get('https://finance.naver.com/sise/lastsearch2.nhn').text
html = BeautifulSoup(raw, 'html.parser')

stocks = html.select('a.tltle')

for stock in stocks:
    print(stock.text)
