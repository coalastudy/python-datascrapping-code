subjects = ['파이썬', '자바스크립트', '루비', '코틀린', '자바스크립트', '파이썬',
            '파이썬', 'C++', 'iOS', '파이썬', 'Go', '안드로이드', '파이썬', '루비',
            'C++', 'iOS', '안드로이드', '파이썬', '파이썬', '자바스크립트', '루비',
            '안드로이드', '자바', '파이썬', '파이썬', 'C++', 'iOS', '파이썬',
            'Go', '자바', '파이썬', '루비', 'C++', 'iOS', '안드로이드', '파이썬']

counter = {}

for subject in subjects:
    counter[subject] = 0

for subject in subjects:
    counter[subject] += 1

print(counter)
