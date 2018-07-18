

# ---- 숫자 정렬 해보기 ----

numbers = [94, 23, 64, 39, 25, 10, 63, 6, 234, 34, 63, 4, 86, 5, 24, 1, 631, 90]

# print(sorted(numbers))
# print(numbers)


# ---- 문자 정렬 해보기 ----

alphabets = ['r', 'f', 'w', 'b', 'z', 'n', 'm', 'q', 'i', 'y', 'c']

# print(sorted(alphabets))

words = ['coffee', 'car', 'carpet', 'candy', 'cure', 'crisis', 'cucumber']

# print(sorted(words))

kwords = ['가방', '가면', '가림막', '군인', '누빔', '가판대', '가생이', '경찰', '기업']

# print(sorted(kwords))


# ---- 혼합 정렬 해보기 ----

mixed = [3, '호날두', 'Python', 15, '메시', 'Data']

# print(sorted(mixed))


# ---- dictionary 정렬 해보기 ----

scores = {'h': 16, 'b': 24, 'd': 91, 'c': 138, 'z': 6, 'a': 65}

# print(sorted(scores))
# print(sorted(scores.keys()))
# print(sorted(scores.values()))
# print(sorted(scores.items()))


# ---- 정렬 기준 바꾸어보기 ----

def sortKey(item):
    return item[1]


# print(sorted(scores.items(), key=sortKey))
# print(sorted(scores.items(), key=sortKey, reverse=True))


# ---- 네이버 TV 예제에 적용해보기 ----

chnInfos = {'하트시그널2': {'hit': 20000, 'like': 3800},
            '미스터션샤인': {'hit': 18000, 'like': 2500},
            '쇼미더머니7': {'hit': 25000, 'like': 3200}}


def sortByHit(info):
    return info[1]['hit']


def sortByLike(info):
    return info[1]['like']


# print(sorted(chnInfos.items(), key=sortByHit, reverse=True))
# print(sorted(chnInfos.items(), key=sortByLike, reverse=True))
