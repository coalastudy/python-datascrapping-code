from selenium import webdriver
from selenium import common
from bs4 import BeautifulSoup
import time

driver = None
driver2 = None


def init():
    global driver, driver2
    driver = webdriver.Chrome('./chromedriver')
    driver2 = webdriver.Chrome('./chromedriver')
    driver.get('https://map.naver.com/')

    print('검색 키워드를 입력해주세요.')
    keyword = input()
    driver.find_element_by_id('search-input').send_keys(keyword)

    driver.find_element_by_css_selector('#header > div.sch > fieldset > button').click()


def extract_list():
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select('ul.lst_site > li')


def handle_list_data(data):

    title = addr = tel = ''
    try:
        title = data.select_one('a').text
        addr = data.select_one('.addr').text[:-3].strip()
        tel = data.select_one('.tel').text.strip()

        detail_url = data.select_one('a.spm_sw_detail').attrs['href']
        handle_detail_data(detail_url)

        print('---------------')
        time.sleep(1)

    except:
        tel = ''

    finally:
        print(title, '/', addr, '/', tel)


def handle_detail_data(url):
    driver2.get('https://map.naver.com' + url)
    times = driver2.find_elements_by_css_selector('.section_detail_time li')
    for t in times:
        print(t.text)


def click_next_page(page):
    if page % 5 == 1:
        driver.find_element_by_class_name('next').click()
    else:
        driver.find_element_by_xpath('//a[text()=' + str(page) + ']').click()


def execute():

    init()
    page = 1

    while True:
        list = extract_list()

        for data in list:
            handle_list_data(data)

        page = page + 1

        try:
            click_next_page(page)

        except common.exceptions.NoSuchElementException:
            break
