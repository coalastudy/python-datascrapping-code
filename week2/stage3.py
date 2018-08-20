

cities = ['서울', '인천', '수원', '성남', '대전', '원주', '대구', '김해', '군산', '경주', '청주']

print(cities)

print(cities[0])
print(cities[3])
print(cities[7])
print(cities[1] + '국제공항')
cities[2] = '안양'
print(cities)

citiesLandmark = ['서울', ['롯데타워', '청와대'], '인천', ['인천국제공항', '차이나타운'], '수원', ['수원 화성', '박지성로'],
                  '성남', ['네이버', '판교 현대백화점'], '대전', ['성심당', '대전엑스포']]

print(citiesLandmark[1])
print(citiesLandmark[1][0])

cities = ['서울', '인천', '수원', '성남', '대전', '원주', '대구', '김해', '군산', '경주', '청주']

print(cities[0:3])
print(cities[4:6])

print(cities[5:])   # 5번 ~ 끝
print(cities[:4])   # 처음 ~ 3번
print(cities[-1])   # 끝에서 첫번째
print(cities[1:-1]) # 두번째 ~ 끝에서 첫번째


price = '가격 : 13,000 원'
print(price[-14])
# price = price[5:-2]
# print(price)

hit = '조회 수 - 139.153회'