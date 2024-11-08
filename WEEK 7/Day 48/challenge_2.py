from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe"
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get('https://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.XPATH, '/html/body/form/input[1]')
fname.send_keys("Daniel")
# fname.send_keys(Keys.ENTER)
# print(fname.text)
lname = driver.find_element(By.XPATH, '/html/body/form/input[2]')
lname.send_keys('Samson')
# lname.send_keys(Keys.ENTER)

email = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email.send_keys("Dansam123@test.com")
# email.send_keys(Keys.ENTER)

submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()
# submit.send_keys(Keys.ENTER)



driver.close()
driver.quit()