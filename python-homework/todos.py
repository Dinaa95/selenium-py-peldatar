from selenium import webdriver
PATH = 'C:\Programs\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(PATH)

URL = 'http://localhost:9999/todo.html'
browser.get(URL)

elements = browser.find_elements_by_xpath('//li/span')
for i in elements:
    print(i.text)

browser.quit()
