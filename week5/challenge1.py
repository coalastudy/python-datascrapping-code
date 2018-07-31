from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.naver.com')

driver.find_element_by_id('id').send_keys('doomsdt')
driver.find_element_by_id('pw').send_keys('5891421lL!')
driver.find_element_by_css_selector('span.btn_login').click()

driver.find_element_by_css_selector('a.mn_mail').click()
