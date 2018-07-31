from selenium import webdriver
from selenium import common
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
driver2 = webdriver.Chrome('./chromedriver')

driver.get('https://map.naver.com/')

driver.find_element_by_id('search-input').send_keys('신촌 스터디룸')

driver.find_element_by_css_selector('#header > div.sch > fieldset > button').click()

page = 1

while True:
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    list = soup.select('ul.lst_site > li')

    for data in list:

        title = data.select_one('a').text

        print(title)

        detail_url = data.select_one('a.spm_sw_detail').attrs['href']
        driver2.get('https://map.naver.com' + detail_url)
        times = driver2.find_elements_by_css_selector('.section_detail_time li')
        for t in times:
            print(t.text)

        print('---------------')
        time.sleep(1)

    page = page + 1

    try:
        if page % 5 == 1:
            driver.find_element_by_class_name('next').click()
        else:
            driver.find_element_by_xpath('//a[text()=' + str(page) + ']').click()

    except common.exceptions.NoSuchElementException:
        break

    time.sleep(1)
