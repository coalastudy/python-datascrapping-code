

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
    mall = item.select_one('div.info_mall > p.mall_txt > a.mall_img')

    try:
        mall_name = mall.attrs['title']
    except:
        mall_name = mall.text

    mall_name = mall_name.split(' ')[0]

    print(rank, name, price, reload, star, comments, mall_name)
