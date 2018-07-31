from selenium import webdriver
from selenium import common
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.naver.com/')

# driver.find_element_by_id('search').send_keys('프로듀스 48')
# driver.find_element_by_id('search-icon-legacy').click()
# time.sleep(1)
# videos = driver.find_elements_by_tag_name('ytd-video-renderer')
#
# for video in videos:
#     print(1)
#     # print(video.text)
#     print(video.find_element_by_css_selector('a#video-title').text)

time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
