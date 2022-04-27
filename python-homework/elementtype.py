from selenium import webdriver
import selenium
import time
PATH = 'C:\Programs\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(PATH)


URL = 'http://localhost:9999/trickyelements.html'
browser.get(URL)


try:
    random_button = browser.find_element_by_tag_name('button')
    time.sleep(3)
except selenium.common.exceptions.NoSuchElementException:
    browser.refresh()
#    print('Ilyen elem nincs az oldalon')
else:
    print('Successfully found a button')
    random_button.click()

time.sleep(2)
browser.close()
