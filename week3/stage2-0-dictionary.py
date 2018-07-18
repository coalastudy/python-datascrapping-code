# ---- dictionary 기본 구성 & 조회 ----

people = {'korean': 380, 'american': 42, 'japanese': 15}
#
# print(people)
# print(people['korean'])
#
# people['american'] = 63
#
# print(people['american'])
# print(people['japanese'])


# ---- 중첩 dictionary 구조 ----

chnInfos = {'하트시그널2': {'hit': 20000, 'like': 3800},
            '미스터션샤인': {'hit': 18000, 'like': 3500},
            '쇼미더머니7': {'hit': 25000, 'like': 2200}}
#
# print(chnInfos)
# print(chnInfos['하트시그널2'])
# print(chnInfos['미스터션샤인']['hit'])


# ---- 중첩 dictionary 수정 ----

chnInfos['하트시그널2']['hit'] = chnInfos['하트시그널2']['hit'] + 4900
chnInfos['하트시그널2']['like'] += 280

# print(chnInfos['하트시그널2'])


# ---- 중첩 dictionary 추가 ----

newchn = '꽃보다할배'
newhit = 19400
newlike = 2760

chnInfos[newchn]['hit'] += 1300
chnInfos[newchn]['like'] += 110
# chnInfos[newchn] = {'hit': newhit, 'like': newlike}

print(chnInfos)