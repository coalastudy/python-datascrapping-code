import requests
from bs4 import BeautifulSoup
import datetime
import openpyxl

req = requests.get('https://tv.naver.com/r/')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')

print(html)
#
# infos = html.select('.cds_info')
# chnInfos = {}
#
# excel = openpyxl.Workbook()
# sheet = excel.active
# sheet.title = '조회수별 정렬'
#
#
# for info in infos:
#     chn = info.select('dd.chn > a')[0].text
#     hit = int(info.select('span.hit')[0].text[4:].replace(',', ''))
#     like = int(info.select('span.like')[0].text[5:].replace(',', ''))
#
#     if chn not in chnInfos.keys():
#         chnInfos[chn] = {'hit': hit, 'like': like}
#     else:
#         chnInfos[chn]['hit'] += hit
#         chnInfos[chn]['like'] += like
#
#
# def sortKey(item):
#     return item[1]['hit']
#
#
# sortedList = sorted(chnInfos.items(), key=sortKey, reverse=True)
#
# for sortedInfo in sortedList:
#     sheet.append([sortedInfo[0], sortedInfo[1]['hit'], sortedInfo[1]['like']])
#
# dt = datetime.datetime.now()
# filename = dt.strftime("TOP_100_%Y_%m_%d")
#
# excel.save(filename + '.xlsx')
