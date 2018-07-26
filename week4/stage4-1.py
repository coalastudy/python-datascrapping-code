
from urllib import request, parse
from bs4 import BeautifulSoup

page = 1

req = request.Request('https://search.naver.com/search.naver?&where=news&query=' + parse.quote('아시안게임') + '&start=1&pd=12', headers={'User-Agent': 'Mozilla/5.0'})
raw = request.urlopen(req).read()
html = BeautifulSoup(raw, 'html.parser')
total = int(html.select_one('.all_my').text.split('/')[1][:-1].replace(',', ''))

print('total = ', total)

while (page-1) * 10 < total:
    print('-------------------- page', page, '--------------------')
    req = request.Request('https://search.naver.com/search.naver?&where=news&query=' + parse.quote('아시안게임') + '&start=' + str((page - 1) * 10 + 1) + '&pd=12', headers={'User-Agent': 'Mozilla/5.0'})
    raw = request.urlopen(req).read()
    html = BeautifulSoup(raw, 'html.parser')

    list = html.select('.type01 dl')

    for article in list:
        journal = article.select_one('span._sp_each_source').text
        title = article.select_one('dt').text

        print(journal, title)

    page = page + 1
