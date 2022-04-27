from selenium import webdriver
import selenium
import time
PATH = 'C:\Programs\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(PATH)


URL = 'https://idokep.hu'
browser.get(URL)

try:
    bad = browser.find_element_by_id('random')
except selenium.common.exceptions.NoSuchElementException:
    print('Ilyen elem nincs az oldalon')
else:
    print('Success')

time.sleep(2)
browser.quit()
