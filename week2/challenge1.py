
raw_data = '    코알라 웹개발 스터디에 정상적으로 신청이 완료되었습니다.    '

data = raw_data.strip()
new_data = data.replace('웹개발', '데이터 수집')
data_length = len(new_data)

print(raw_data)
print(data)
print(new_data)
print(data_length)

print(len(raw_data.strip().replace('웹개발', '데이터 수집')))