from selenium import webdriver
from selenium import common
import time
import datetime
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

driver.get('https://map.naver.com/')

keyword = input("키워드를 입력해주세요!\n")

driver.find_element_by_id('search-input').send_keys(keyword)

driver.find_element_by_css_selector('#header > div.sch > fieldset > button').click()

page = 0

start = datetime.datetime.now()

while True:

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    list = soup.select('.lsnx_det')
    # datas = list.find_elements_by_class_name('lsnx_det')
    page = page + 1

    for data in list:

        try:
            title = data.select_one('a').text
            addr = data.select_one('.addr').text[:-3].strip()
            tel = data.select_one('.tel').text.strip()

        except:
            tel = ''

        finally:
            print(title, '/', addr, '/', tel)

    index = page % 5 + 1

    if index == 1:
        index = index + 5

    try:
        driver.find_element_by_class_name('paginate').find_elements_by_css_selector('*')[index].click()
        time.sleep(1)
    except:
        break

print(datetime.datetime.now() - start, "s elapsed.")