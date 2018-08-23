import requests
from bs4 import BeautifulSoup

for page in range(1, 6):
    req = requests.get('https://search.shopping.naver.com/search/category.nhn?cat_id=50001203&pagingSize=40&pagingIndex=' + str(page))
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')

    items = html.select('li._itemSection')

    for item in items:
        name = item.select_one('a.tit').text.strip()
        price = item.select_one('span.price span.num').text
        register_date = item.select_one('span.date').text

        print(name, '/', price, '/', register_date)
