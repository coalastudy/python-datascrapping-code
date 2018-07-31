import openpyxl
import requests
from bs4 import BeautifulSoup

# 프로그램의 전체 흐름을 총괄합니다.
def execute():
    company_items = {}

    for page in range(1, 11):
        html = scrap_page(page)
        items = extract_list(html)

        for item in items:
            infos = extract_data(item)
            acc_info(company_items, infos)

    save_excel(company_items)


# scrap_page
# 웹에서 HTML 문서를 추출하여 돌려줍니다.
# INPUT
# page - 추출할 페이지의 번호
# OUTPUT
# html - 추출된 HTML 값
def scrap_page(page):
    req = requests.get('https://search.shopping.naver.com/search/category.nhn?cat_id=50001203&pagingSize=40&pagingIndex=' + str(page))
    raw = req.text
    html = BeautifulSoup(raw, 'html.parser')
    return html


# extract_list
# HTML 값에서 물품 리스트를 추출하여 돌려줍니다.
# INPUT
# html - 원본 HTML 값
# OUTPUT
# items - 물품 리스트
def extract_list(html):
    items = html.select('li._itemSection')
    return items


# extract_data
# 물품 HTML에서 필요한 정보를 추출하여 돌려줍니다.
# INPUT
# item - 추출할 물품 HTML 값
# OUTPUT
# rank, name, price, reload, star, comments, mall_name 을 키로 가지고 있는 dictionary
def extract_data(item):
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
    return { 'rank': rank, 'name': name, 'price': price, 'reload': reload, 'star': star, 'comments': comments, 'mall_name': mall_name }


# acc_info
# dictionary 형태의 단일 물품 정보를 전체 dictionary에 누적합니다.
# INPUT
# company_items - 정보를 누적시킬 전체 dictionary
# infos - 단일 물품 정보를 담은 dictionary
# OUTPUT
#
def acc_info(company_items, infos):
    mall_name = infos['mall_name']
    if mall_name in company_items.keys():
        company_items[mall_name].append(infos)
    else:
        company_items[mall_name] = [infos]


# save_excel
# 누적된 정보를 엑셀에 저장합니다.
# INPUT
# company_items - 쇼핑 물품 정보가 누적되어있는 전체 dictionary
# OUTPUT
#
def save_excel(company_items):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['제조사', '순위', '품명', '최저가', '가격 갱신일', '만족도', '후기 수'])

    for company_item in company_items.items():
        ws.append([company_item[0]])

        for item in company_item[1]:
            ws.append(['', item['rank'], item['name'], item['price'], item['reload'], item['star'], item['comments']])

        ws.append([])

    wb.save('mouse.xlsx')
