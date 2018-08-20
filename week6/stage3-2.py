from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')

driver.get('https://map.naver.com/')

driver.find_element_by_id('search-input').send_keys('신촌 스터디룸')

driver.find_element_by_css_selector('#header > div.sch > fieldset > button').click()

page = 1

while True:
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    list = soup.select('.lsnx_det')

    for data in list:

        try:
            title = data.select_one('a').text
            addr = data.select_one('.addr').text.replace('지번', '').strip()
            tel = data.select_one('.tel').text.strip()

        except:
            tel = ''

        finally:
            print(title, '/', addr, '/', tel)

    page = page + 1

    try:
        if page % 5 == 1:
            driver.find_element_by_class_name('next').click()
        else:
            driver.find_element_by_xpath('//a[text()=' + str(page) + ']').click()

    except:
        break

    time.sleep(1)
