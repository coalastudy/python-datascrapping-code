import requests
from urllib import parse
from bs4 import BeautifulSoup

journalTitles = {}

for i in range(3):
    req = requests.get('https://search.naver.com/search.naver?&where=news&query=' + parse.quote('아시안게임') + '&start=' + str(i * 10 + 1),
                          headers={'User-Agent': 'Mozilla/5.0'})
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')

    list = html.select('.type01 dl')

    for article in list:
        journal = article.select_one('span._sp_each_source').text
        title = article.select_one('dt').text

        if journal not in journalTitles.keys():
            journalTitles[journal] = []
            journalTitles[journal].append(title)
        else:
            if title not in journalTitles[journal]:
                journalTitles[journal].append(title)

for key in journalTitles:
    print(key, journalTitles[key])
