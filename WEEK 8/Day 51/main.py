from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
from dotenv import load_dotenv

load_dotenv('.env')

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe'
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
USERNAME = os.getenv("USER_NAME")


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.driver = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.driver)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()
        time.sleep(3)
        cont = (self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        cont.click()

        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        time.sleep(45)
        self.up = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"Download = {self.down} Mbps")
        print(f"Upload = {self.up} Mbps")
        sleep(2)
        twitter_bot.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.maximize_window()

        self.driver.get('https://x.com/i/flow/login')
        time.sleep(5)
        email = self.driver.find_element(By.XPATH,
                                         value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(2)

        username = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        if username:
            username.send_keys(USERNAME) #this line check if the username is required, you should put yours. YES
            username.send_keys(Keys.ENTER)
        time.sleep(5)

        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(25)
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        sleep(3)
        tweet = self.driver.find_element(By.XPATH,
                                         value= '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]')
        tweet.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down} Mbps Down/{self.up} Mbps Up when I pay for {PROMISED_DOWN} Mbps Down/{PROMISED_UP} Mbps Up?")
        sleep(5)
        self.driver.find_element(By.XPATH,
                                 value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span').click()
        sleep(2)
        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
twitter_bot.get_internet_speed()
# twitter_bot.tweet_at_provider()