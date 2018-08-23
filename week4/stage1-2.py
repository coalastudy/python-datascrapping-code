
people = {'korean': 380, 'american': 42, 'japanese': 15, 'german': 26, 'french': 7, 'chinese': 213, 'canadian': 11}

print(people.keys())
print(people.values())
print(people.items())


for p_item in people.items():
    print('There are', p_item[1], p_item[0] + 's')



chnInfos = {'하트시그널2': {'hit': 20000, 'like': 3800},
            '미스터션샤인': {'hit': 18000, 'like': 3500},
            '쇼미더머니7': {'hit': 25000, 'like': 2200}}

print(chnInfos.keys())
print(chnInfos.values())
print(chnInfos.items())


for chn_info in chnInfos.items():
    print(chn_info[0], '의 조회수는', chn_info[1]['hit'], '입니다.')

# print('꽃보다할배' in chnInfos.keys())
# print('하트시그널2' in chnInfos.keys())


# ---- 네이버TV 예제에 응용하기 ----

# newchn = '꽃보다할배'
#
# if newchn in chnInfos.keys():
#     print('처음 수집된 채널')
# else:
#     print('이미 수집된 채널')
