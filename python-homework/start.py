from selenium import webdriver
import time
PATH = 'C:\Programs\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(PATH)


URL = 'https://idokep.hu'
browser.get(URL)
time.sleep(2)
cookie_accept = browser.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
if cookie_accept.is_displayed():
    cookie_accept.click()
