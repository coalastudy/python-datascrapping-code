import requests
from bs4 import BeautifulSoup

req = requests.get('https://tv.naver.com/r/')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')
infos = html.select('.cds_info')

dict = {}

totalHit = 0
totalLike = 0


def extractInfos(info):
    title = info.select('dt.title')[0].text.strip()
    chn = info.select('dd.chn')[0].text.strip()
    hit = int(info.select('span.hit')[0].text[4:].replace(',', ''))
    like = int(info.select('span.like')[0].text[5:].replace(',', ''))

    return title, chn, hit, like


def insertOrNew(dict, chn, hit, like):
    if chn not in dict:
        dict[chn] = {'hit': hit, 'like': like}
    else:
        dict[chn]['hit'] += hit
        dict[chn]['like'] += like

    return dict


def calculateConstants(totalA, totalB, size):
    averageA = totalA / size
    averageB = totalB / size

    if averageA > averageB:
        weight = averageA / averageB
        averageScore = averageB * weight + averageA
    else:
        weight = averageB / averageA
        averageScore = averageA * weight + averageB

    return weight, averageScore


def calculateScore(a, b, w, avr):
    if a > b:
        return round(((b * w) + a) * 50 / avr, 2)
    else:
        return round(((a * w) + b) * 50 / avr, 2)


for info in infos:
    title, chn, hit, like = extractInfos(info)

    totalHit += hit
    totalLike += like

    dict = insertOrNew(dict, chn, hit, like)


w, avr = calculateConstants(totalHit, totalLike, len(infos))

for prog in dict:
    dict[prog]['score'] = calculateScore(dict[prog]['hit'], dict[prog]['like'], w, avr)


sortedList = sorted(dict, key=lambda x: dict[x]['score'], reverse=True)


for prog in sortedList:
    print(prog, dict[prog])
