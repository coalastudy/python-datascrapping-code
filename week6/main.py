
import tv
import map
import news


def print_menu():
    print('---------------------------------')
    print('수집할 대상을 선택해주세요.')
    print('1. 네이버 TV')
    print('2. 네이버 뉴스')
    print('3. 네이버 지도')
    print('4. 종료')
    print('---------------------------------')

while True:
    print_menu()
    select = input()

    if select == '1':
        tv.execute()
    elif select == '2':
        news.execute()
    elif select == '3':
        map.execute()
    elif select == '4':
        break
    else:
        print('잘못된 입력입니다.')
