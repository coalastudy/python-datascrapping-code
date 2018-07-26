import requests
from bs4 import BeautifulSoup
import datetime
import openpyxl

req = requests.get('https://tv.naver.com/r/')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')


infos = html.select('.cds_info')
chnInfos = {}

# ---- 엑셀 파일 초기화 ----

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = '조회수별 정렬'

# -------------------------

for info in infos:
    chn = info.select_one('dd.chn > a').text
    hit = int(info.select_one('span.hit').text[4:].replace(',', ''))
    like = int(info.select_one('span.like').text[5:].replace(',', ''))

    if chn in chnInfos.keys():
        chnInfos[chn]['hit'] += hit
        chnInfos[chn]['like'] += like
    else:
        chnInfos[chn] = {'hit': hit, 'like': like}


def sortKey(item):
    return item[1]['hit']


sortedList = sorted(chnInfos.items(), key=sortKey, reverse=True)

for sortedInfo in sortedList:
    sheet.append([sortedInfo[0], sortedInfo[1]['hit'], sortedInfo[1]['like']])

dt = datetime.datetime.now()
filename = dt.strftime("TOP_100_%Y_%m_%d") + '.xlsx'

excel.save(filename)
excel.close()
