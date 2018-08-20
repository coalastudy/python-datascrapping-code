from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome('./chromedriver')


# ---- 페이지 접속 ----

driver.get('https://map.naver.com/')


# ---- 요소 탐색, 키보드 입력 ----

driver.find_element_by_id('search-input').send_keys('신촌 스터디룸')


# ---- 요소 탐색, 마우스 클릭 ----

driver.find_element_by_css_selector('#header > div.sch > fieldset > button').click()


# ---- 페이지 수집 ----

list = driver.find_elements_by_css_selector('.lsnx_det')

for data in list:
    print(data.find_element_by_tag_name('a').text)


# ---- 정적 수집으로 전환 ----

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# list = soup.select('.lsnx_det')
#
# for data in list:
#
#     try:
#         title = data.select_one('a').text
#         addr = data.select_one('.addr').text[:-3].strip()
#         tel = data.select_one('.tel').text.strip()
#
#     except:
#         tel = ''
#
#     finally:
#         print(title, '/', addr, '/', tel)
#
