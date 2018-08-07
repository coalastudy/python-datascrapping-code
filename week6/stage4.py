
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import threading

engKor = []

def processMany(start, end):
    driver = webdriver.Chrome('./chromedriver')

    for n in range(start, end + 1):

        req = requests.get('https://news.ycombinator.com/news?p=' + str(n))
        html = BeautifulSoup(req.text, 'html.parser')

        titles = html.select('a.storylink')

        driver.get('https://papago.naver.com/')


        for title in titles:
            orig = title.text
            driver.find_element_by_css_selector('textarea#txtSource').send_keys(title.text)
            driver.find_element_by_css_selector('button#btnTranslate').click()
            time.sleep(1)
            translated = driver.find_element_by_css_selector('div#txtTarget').text
            print(orig, translated)
            engKor.append([orig, translated])
            driver.find_element_by_css_selector('textarea#txtSource').clear()


start_time = time.time()

t1 = threading.Thread(target=processMany, args=(1, 6))
t2 = threading.Thread(target=processMany, args=(6, 11))
t3 = threading.Thread(target=processMany, args=(11, 15))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


print("--- %s seconds ---" % (time.time() - start_time))
