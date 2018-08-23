import requests
from bs4 import BeautifulSoup

price_items = {}

for page in range(1, 6):
    req = requests.get('https://search.shopping.naver.com/search/category.nhn?cat_id=50001203&pagingSize=40&pagingIndex=' + str(page))
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')

    items = html.select('li._itemSection')

    for item in items:
        name = item.select_one('a.tit').text.strip()
        price = int(item.select_one('span.price span.num').text.replace(',',''))
        register_date = item.select_one('span.date').text

        price_range = str(price // 10000) + '만원대'

        if price_range in price_items.keys():
            price_items[price_range].append({
                'name': name, 'price': price, 'register_date': register_date
            })
        else:
            price_items[price_range] = [{
                'name': name, 'price': price, 'register_date': register_date
            }]


for price in price_items.items():
    print(price)
