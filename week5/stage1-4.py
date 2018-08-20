import requests
from bs4 import BeautifulSoup
import datetime

req = requests.get('https://tv.naver.com/r/')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')
chnInfos = {}


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

dt = datetime.datetime.now()
filename = 'TOP100_' + dt.strftime("%Y_%m_%d")
f = open(filename + '.csv', 'w')

for sortedInfo in sortedList:
    f.write(sortedInfo[0] + ',' + str(sortedInfo[1]['hit']) + '\n')

f.close()
