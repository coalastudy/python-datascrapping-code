import requests
from bs4 import BeautifulSoup

journal_articles = {}

for i in range(3):
    raw = requests.get('https://search.naver.com/search.naver?&where=news&query=아시안게임&start=' + str(i * 10 + 1), headers={'User-Agent': 'Mozilla/5.0'}).text
    html = BeautifulSoup(raw, 'html.parser')

    list = html.select('.type01 > li')

    for article in list:
        journal = article.select_one('span._sp_each_source').text
        title = article.select_one('a._sp_each_title').text

        if journal in journal_articles.keys():
            journal_articles[journal].append(title)
        else:
            journal_articles[journal] = [title]

for item in journal_articles.items():
    print(item)
