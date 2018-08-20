import requests
from bs4 import BeautifulSoup
import datetime
import openpyxl

raw = requests.get('https://tv.naver.com/r/').text
html = BeautifulSoup(raw, 'html.parser')

# ---- 엑셀 파일 초기화 ----

excel = openpyxl.Workbook()
clips_sheet = excel.active
clips_sheet.title = 'TOP 100 클립'

clips_sheet.append(['클립 제목', '채널', '조회수', '좋아요 수'])

# -------------------------

infos = html.select('.cds_info')
chnInfos = {}

for info in infos:
    title = info.select_one('dt.title tooltip').text
    chn = info.select_one('dd.chn > a').text
    hit = int(info.select_one('span.hit').text[4:].replace(',', ''))
    like = int(info.select_one('span.like').text[5:].replace(',', ''))

    if chn in chnInfos.keys():
        chnInfos[chn]['hit'] += hit
        chnInfos[chn]['like'] += like
    else:
        chnInfos[chn] = {'hit': hit, 'like': like}

    clips_sheet.append([title, chn, hit, like])


def sortKey(item):
    return item[1]['hit']


sortedList = sorted(chnInfos.items(), key=sortKey, reverse=True)


dt = datetime.datetime.now()
filename = dt.strftime("TOP_100_%Y_%m_%d") + '.xlsx'

excel.save(filename)
excel.close()
