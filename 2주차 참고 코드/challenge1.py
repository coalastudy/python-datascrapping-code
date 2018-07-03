
def makeAmericano():
    print("에스프레소 샷 추출")
    print("얼음 넣기")
    print("물 붓기")
    print("에스프레소 붓기")
    return "아메리카노"

# def makeGuatemalaDripCoffee():
#     print("과테말라 원두 투입")
#     print("드리핑")
#
#
# def makeColombiaDripCoffee():
#     print("콜롬비아 원두 투입")
#     print("드리핑")
#
# def makeChileDripCoffee():
#     print("칠레 원두 투입")
#     print("드리핑")


def makeDripCoffee(bean):
    print(bean, "원두 투입")
    print("드리핑")
    return bean + " 드립커피"


def notifyCustomer(order):
    print("-----------------------------------------")
    print(len("-----------------------------------------"))
    print("주문하신", order, "나왔습니다!")
    print("-----------------------------------------")


notifyCustomer(makeAmericano())
notifyCustomer(makeDripCoffee("과테말라"))
notifyCustomer(makeDripCoffee("콜롬비아"))
notifyCustomer(makeDripCoffee("칠레"))