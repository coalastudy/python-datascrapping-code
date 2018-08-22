
import requests
from bs4 import BeautifulSoup


for i in range(3):
    raw = requests.get('https://news.ycombinator.com/news?p=' + str(i + 1)).text
    html = BeautifulSoup(raw, 'html.parser')

    titles = html.select('a.storylink')

    for title in titles:
        print(title.text)
