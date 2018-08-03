import requests
from bs4 import BeautifulSoup
import openpyxl


wb = openpyxl.Workbook()
ws = wb.active

companyItems = {}

for page in range(1, 10):
    req = requests.get('https://search.shopping.naver.com/search/category.nhn?cat_id=50001203&pagingSize=40&pagingIndex=' + str(page))
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

        if mall_name in companyItems.keys():
            companyItems[mall_name].append({
                'rank': rank, 'name': name, 'price': price, 'reload': reload, 'star': star, 'comments': comments, 'mall_name': mall_name
            })
        else:
            companyItems[mall_name] = [{
                'rank': rank, 'name': name, 'price': price, 'reload': reload, 'star': star, 'comments': comments, 'mall_name': mall_name
            }]
        # print(rank, name, price, reload, star, comments, mall_name)
        # ws.append([rank, name, price, reload, star, comments, mall_name])

ws.append(['제조사', '순위', '품명', '최저가', '가격 갱신일', '만족도', '후기 수'])

for companyItem in companyItems.items():
    ws.append([companyItem[0]])

    for item in companyItem[1]:
        ws.append(['', item['rank'], item['name'], item['price'], item['reload'], item['star'], item['comments']])

    ws.append([])


wb.save('mouse.xlsx')
