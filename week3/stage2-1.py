import requests
from bs4 import BeautifulSoup


req = requests.get('https://tv.naver.com/r/')

raw = req.text

html = BeautifulSoup(raw, 'html.parser')

infos = html.select('.cds_info')

channels = []
hits = []
likes = []

for info in infos:
    chn = info.select('dd.chn > a')[0].text
    hit = int(info.select('span.hit')[0].text[4:].replace(',', ''))
    like = int(info.select('span.like')[0].text[5:].replace(',', ''))

    if chn in channels:
        idx = channels.index(chn)
        hits[idx] = hits[idx] + hit
        likes[idx] = likes[idx] + like

    else:  # channels 배열 안에 현재 chn이 없다.
        channels.append(chn)
        hits.append(hit)
        likes.append(like)

for channel in channels:
    idx = channels.index(channel)
    print(channel, '/', hits[idx], '/', likes[idx])