chnInfos = {'하트시그널2': {'hit': 20000, 'like': 3800},
            '미스터션샤인': {'hit': 18000, 'like': 3500},
            '쇼미더머니7': {'hit': 25000, 'like': 2200}}

# ---- dictionary의 변형 이해 ----

print(chnInfos.keys())
print(chnInfos.values())
print(chnInfos.items())

print('꽃보다할배' in chnInfos.keys())
print('하트시그널2' in chnInfos.keys())


# ---- 네이버TV 예제에 응용하기 ----

newchn = '꽃보다할배'

if newchn in chnInfos.keys():
    print('처음 수집된 채널')
else:
    print('이미 수집된 채널')
