
# ---------------------------------------------------------------
# Challenge 1-1 : makeDripCoffee() 함수의 출력값 만들기
# ---------------------------------------------------------------

def makeAmericano():
    print("에스프레소 샷 추출")
    print("얼음 넣기")
    print("물 붓기")
    print("에스프레소 붓기")
    return "아메리카노"

def makeDripCoffee(bean):
    print(bean, "원두 투입")
    print("드리핑")
    return bean + " 드립커피"

# print("주문하신", makeAmericano(), "나왔습니다!")
# print("주문하신", makeDripCoffee("과테말라"), "나왔습니다!")
# print("주문하신", makeDripCoffee("콜롬비아"), "나왔습니다!")
# print("주문하신", makeDripCoffee("칠레"), "나왔습니다!")

# ---------------------------------------------------------------
# Challenge 1-2 : 출력함수 notifyCustomer() 만들기
# ---------------------------------------------------------------

def notifyCustomer(order):
    print("-----------------------------------------")
    print("주문하신", order, "나왔습니다!")
    print("-----------------------------------------")


notifyCustomer(makeAmericano())
notifyCustomer(makeDripCoffee("과테말라"))
notifyCustomer(makeDripCoffee("콜롬비아"))
notifyCustomer(makeDripCoffee("칠레"))

