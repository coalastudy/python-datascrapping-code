from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

# 로그인 전용 화면
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/')
# 아이디와 비밀번호 입력
driver.find_element_by_name('id').send_keys('doomsdt')
driver.find_element_by_name('pw').send_keys('5891421l;!')
# 로그인 버튼 클릭
driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()
#
# driver.find_element_by_css_selector('a.mn_mail').click()
