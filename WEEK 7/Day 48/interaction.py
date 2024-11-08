from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
# wiki = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(wiki.text)

# find = driver.find_element(By.LINK_TEXT, "View source")
# find.click()

search = driver.find_element(By.NAME, 'search')
# print(search.get_attribute('name'))
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


driver.close()
driver.quit()