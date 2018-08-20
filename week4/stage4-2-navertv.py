import requests
from bs4 import BeautifulSoup


raw = requests.get('https://tv.naver.com/r/').text
html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')
chnInfos = {}

for info in infos:
    chn = info.select_one('dd.chn > a').text
    hit = int(info.select_one('span.hit').text[4:].replace(',', ''))
    like = int(info.select_one('span.like').text[5:].replace(',', ''))

    if chn not in chnInfos.keys():
        chnInfos[chn] = {'hit': hit, 'like': like}
    else:
        chnInfos[chn]['hit'] += hit
        chnInfos[chn]['like'] += like

# for i in chnInfos.items():
#     print(i)


def sortKey(item):
    return item[1]['hit']


sortedList = sorted(chnInfos.items(), key=sortKey, reverse=True)

for sortedInfo in sortedList:
    print(sortedInfo)
