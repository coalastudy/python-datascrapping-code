
numbers = [94, 23, 64, 39, 25, 10, 63, 6, 234, 34, 63, 4, 86, 5, 24, 1, 631, 90]

# print(sorted(numbers))
# print(numbers)

alphabets = ['r', 'f', 'w', 'b', 'z', 'n', 'm', 'q', 'i', 'y', 'c']

# print(sorted(alphabets))

words = ['coffee', 'car', 'carpet', 'candy', 'cure', 'crisis', 'cucumber']

# print(sorted(words))

kwords = ['가방', '가면', '가림막', '군인', '누빔', '가판대', '가생이', '경찰', '기업']

# print(sorted(kwords))

mixed = [3, '호날두', 'Python', 15, '메시', 'Data']

# print(sorted(mixed))

scores = {'h': 16, 'b': 24, 'd': 91, 'c': 138, 'z': 6, 'a': 65}

# for key in scores:
#     print(key, scores[key])

# print(sorted(scores))
# print(scores.keys())


# print(dictionary.items())
# print(scores.values())
#
# print(sorted(scores.values()))
#
# print(scores.items())
#
# print(sorted(scores.items()))


def sortKey(item):
    return item[1]


print(sorted(scores.items(), key=sortKey))

#
#
print(sorted(scores.items(), key=sortKey, reverse=True))
