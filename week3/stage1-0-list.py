
subjects = ["파이썬", "페이스북 웹개발", "데이터 수집", "안드로이드", "알고리즘", "Javascript", "iOS"]

# ---- 리스트 출력과 인덱스를 통한 기초적인 조회 ----
# print(subjects)
# print(subjects[0], subjects[1], subjects[3])
#
# print(subjects[0] + " 스터디", subjects[1] + " 스터디", subjects[2] + " 스터디", subjects[3] + " 스터디",
# subjects[4] + " 스터디", subjects[5] + " 스터디", subjects[6] + " 스터디")


# ---- for 문 ----
#
# for subject in subjects:
#     print(subject, "스터디")


# ---- 리스트 슬라이싱 ----

# upper = subjects[0:3]
#
# for subject in upper:
#     print("[인기]", subject)


# ---- 고급 리스트 슬라이싱 ----

# print(subjects[:3])   # 처음 ~ 2번
# print(subjects[3:])   # 3번 ~ 끝
# print(subjects[:])    # 처음 ~ 끝
#
# print(subjects[-1])    # 끝에서 첫번째
# print(subjects[-3:])   # 끝에서 두개
# print(subjects[2: -2]) # 2번째부터 끝에서 2번째까지


# ---- 리스트로서의 문자열 ----

# str = 'string!'
#
# for s in str:
#     print(s)


# ---- 문자열 슬라이싱 ----
#
# str = 'coala python study'
# print(str[6:12])
# print(str[:6])
# print(str[-5:])
