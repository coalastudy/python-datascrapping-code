import requests
from bs4 import BeautifulSoup


req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')

chnInfos = {}

for info in infos:
    chn = info.select_one('dd.chn > a').text
    hit = int(info.select_one('span.hit').text[4:].replace(',', ''))
    like = int(info.select_one('span.like').text[5:].replace(',', ''))
    score = (hit + like * 350) // 100

    if chn not in chnInfos.keys():
        chnInfos[chn] = {'hit': hit, 'like': like, 'score': score}
    else:
        chnInfos[chn]['hit'] += hit
        chnInfos[chn]['like'] += like
        chnInfos[chn]['score'] += score


def sortKey(item):
    return item[1]['score']


sortedList = sorted(chnInfos.items(), key=sortKey, reverse=True)

for sortedInfo in sortedList:
    print(sortedInfo)
