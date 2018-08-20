
cities = ['서울', '인천', '수원', '성남', '대전', '원주', '대구', '김해', '군산', '경주', '청주']

# print(cities[0] + ' 명소')
# print(cities[1] + ' 명소')
# print(cities[2] + ' 명소')
# print(cities[3] + ' 명소')
# print(cities[4] + ' 명소')
# print(cities[5] + ' 명소')
# print(cities[6] + ' 명소')
# print(cities[7] + ' 명소')
# print(cities[8] + ' 명소')
# print(cities[9] + ' 명소')
# print(cities[10] + ' 명소')

additional = '의 명소를 방문해보세요.'

for city in cities:
    print(city + additional)
    print('-------------------------')


cities.append('김포')
cities.append('순천')
print(cities)

cities.pop(2)
print(cities)

cities.reverse()
print(cities)

cities.sort()
print(cities)