from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe'

chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)


# driver.get('https://www.amazon.com')
driver.get('https://www.python.org')
# search_bar = driver.find_element(By.NAME, 'q')
# print(search_bar.get_attribute('placeholder'))

# logo = driver.find_element(By.CLASS_NAME, 'python-logo')
# print(logo.size)

# doc_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(doc_link.text)

# xpath= driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(xpath.text)



driver.close()
driver.quit()