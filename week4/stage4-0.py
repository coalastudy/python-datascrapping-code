
from urllib import request, parse
from bs4 import BeautifulSoup

page = 1

while (page-1) * 10 < total :
    raw = request.urlopen('https://search.naver.com/search.naver?&where=news&query=' + parse.quote('아시안게임') + '&start=' + str(page * 10 + 1) + '&pd=12')
    html = BeautifulSoup(raw, 'html.parser')

    list = html.select('.type01 dl')

    for article in list:
        journal = article.select_one('span._sp_each_source').text
        title = article.select_one('dt').text

        print(journal, title)

    total = total + 1
