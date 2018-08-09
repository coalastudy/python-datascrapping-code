
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

req = requests.get('https://news.ycombinator.com/news?p=1')
html = BeautifulSoup(req.text, 'html.parser')

titles = html.select('a.storylink')

driver.get('https://papago.naver.com/')


for title in titles:
    print(title.text)
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(title.text)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    translated = driver.find_element_by_css_selector('div#txtTarget').text
    print(translated)
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    time.sleep(1)
