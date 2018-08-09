

import requests
from bs4 import BeautifulSoup

req = requests.get('https://search.shopping.naver.com/search/category.nhn?cat_id=50001203&pagingSize=40&pagingIndex=1')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')

items = html.select('li._itemSection')


for item in items:
    rank = int(item.attrs['data-expose-rank'])
    info = item.select_one('div.info')

    name = info.select_one('a.tit').text.strip()
    price = info.select_one('span.price span.num')
    reload = price.attrs['data-reload-date']
    price = price.text

    try:
        star = info.select_one('span.etc span.star_graph span').attrs['style'][6:]
    except:
        star = '-'

    comments = info.select_one('span.etc em').text
    brand = item.select_one('div.info_mall > p.mall_txt > a.mall_img')

    try:
        brand = brand.attrs['title']
    except:
        brand = brand.text

    brand = brand.split(' ')[0]

    print(rank, name, price, reload, star, comments, brand)
