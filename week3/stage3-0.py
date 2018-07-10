import requests
from bs4 import BeautifulSoup


req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')

channels = []
meta = []

for info in infos:
    chn = info.select('dd.chn > a')[0].text
    hit = int(info.select('span.hit')[0].text[4:].replace(',', ''))
    like = int(info.select('span.like')[0].text[5:].replace(',', ''))

    if chn in channels:
        idx = channels.index(chn)
        meta[idx]['hit'] = meta[idx]['hit'] + hit
        meta[idx]['like'] = meta[idx]['like'] + like

    else:
        channels.append(chn)
        meta.append({'hit': hit, 'like': like})

for channel in channels:
    idx = channels.index(channel)
    print(channel, '/', meta[idx])
