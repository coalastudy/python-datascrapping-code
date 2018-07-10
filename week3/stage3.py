import requests
from bs4 import BeautifulSoup


req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')

dict = {}

totalHit = 0
totalLike = 0

for info in infos:
    title = info.select('dt.title')[0].text.strip()
    chn = info.select('dd.chn')[0].text.strip()

    meta = info.select('dd.meta')[0]
    hit = int(meta.select('span.hit')[0].text[4:].replace(',', ''))
    like = int(meta.select('span.like')[0].text[5:].replace(',', ''))

    # score = int((like + hit / 20) / 100)

    totalHit += hit
    totalLike += like

    if chn not in dict:
        dict[chn] = {'hit': hit, 'like': like}
    else:
        dict[chn]['hit'] += hit
        dict[chn]['like'] += like

averageLike = totalLike / len(infos)
averageHit = totalHit / len(infos)

weight = averageHit / averageLike

avr = averageLike * weight + averageHit


for prog in dict:
    dict[prog]['score'] = round(((dict[prog]['like'] * weight) + dict[prog]['hit']) * 50 / avr, 2)
    print(prog, dict[prog])

