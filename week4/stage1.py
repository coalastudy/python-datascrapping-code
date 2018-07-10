import requests
from bs4 import BeautifulSoup
import datetime

req = requests.get('https://tv.naver.com/r/')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')
chnInfos = {}

dt = datetime.datetime.now()
filename = 'TOP100_' + dt.strftime("%Y_%m_%d")
f = open(filename + '.csv', 'w')

for info in infos:
    chn = info.select('dd.chn > a')[0].text
    hit = int(info.select('span.hit')[0].text[4:].replace(',', ''))
    like = int(info.select('span.like')[0].text[5:].replace(',', ''))

    if chn not in chnInfos.keys():
        chnInfos[chn] = {'hit': hit, 'like': like}
    else:
        chnInfos[chn]['hit'] += hit
        chnInfos[chn]['like'] += like


def sortKey(item):
    return item[1]['hit']


sortedList = sorted(chnInfos.items(), key=sortKey, reverse=True)

for sortedInfo in sortedList:
    f.write(sortedInfo[0] + ',' + str(sortedInfo[1]['hit']) + '\n')

f.close()
