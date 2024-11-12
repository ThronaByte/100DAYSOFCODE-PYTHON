import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec

# Load environment variables
load_dotenv(".env")

# Constants
CHROME_DRIVER_PATH = 'C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe'
SIMILAR_ACCOUNT = 'freecodecamp'
USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')


class InstaFollower:
    def __init__(self):
        # Initialize Chrome WebDriver
        self.driver_service = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.NAME, "username"))
        )

        #  username
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(USERNAME)
        time.sleep(1)

        #  password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.RETURN)

        # Wait until the main page loads
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Home']"))
        )

    def find_followers(self):
        # Navigate to the similar account's followers list
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))
        )

        # Open the followers modal
        followers_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        followers_button.click()

        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

        # Scroll back to the top
        self.driver.execute_script("arguments[0].scrollTop = 0", modal)
        time.sleep(2)

    def follow(self):
        time.sleep(2)
        print("Attempting to click follow buttons...")
        follow_buttons = self.driver.find_elements(By.CLASS_NAME, "_ap3a _aaco _aacw _aad6 _aade")

        for button in follow_buttons:
            try:
                button.click()
                print("Clicked 'Follow'")
                time.sleep(2)
            except ElementClickInterceptedException:
                # Handle pop-up with "Cancel" button if it appears
                try:
                    cancel_button = WebDriverWait(self.driver, 5).until(
                        ec.element_to_be_clickable((By.CLASS_NAME, "_abm0"))
                    )
                    cancel_button.click()
                    print("Cancelled pop-up")
                    time.sleep(3)
                except Exception as e:
                    print(f"Error handling pop-up: {e}")
            except Exception as e:
                print(f"Error clicking follow button: {e}")


# Run the bot
instabot = InstaFollower()
instabot.login()
instabot.follow()
instabot.find_followers()
