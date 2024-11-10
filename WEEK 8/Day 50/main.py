from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv('.env')

FB_MAIL = os.getenv("FB_MAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")


chrome_driver_path = 'C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe'
chrome_server = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_server)

driver.get('https://tinder.com/')

# sleep(2)


sleep(2)
login_button = driver.find_element(By.XPATH, value= '//*[@id="s546717130"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="s-1181663946"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

fb_email = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_email.send_keys(FB_MAIL)
fb_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_password.send_keys(FB_PASSWORD)
fb_password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()

