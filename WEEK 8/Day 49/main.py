from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")


service = Service("C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)


URL = 'https://www.linkedin.com/jobs/search/?currentJobId=4072104102&f_AL=true&f_E=4&f_TPR=r86400&geoId=105015875&keywords=python'
driver.get(URL)

# Sign-in
wait = WebDriverWait(driver, 5)
# time.sleep(5)
try:
    # sign_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
    # sign_in_button.click()

    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')))
    sign_in_button.click()


    email_field = wait.until(EC.presence_of_element_located((By.NAME, "session_key")))
    email_field.send_keys(MY_EMAIL)
    password_field = driver.find_element(By.NAME, "session_password")
    password_field.send_keys(MY_PASSWORD)
    password_field.send_keys(Keys.ENTER)

    time.sleep(13)

    # Find job postings
    jobs = driver.find_elements(By.CLASS_NAME, 'job-card-list__title')
    jobs_available = [job.text for job in jobs]
    print("Jobs found:", jobs_available)

    # Loop through jobs and apply
    while jobs_available:
        posting_num = 0
        try:
            job_element = driver.find_element(By.LINK_TEXT, f'{jobs_available[posting_num]}')
            job_element.click()
            time.sleep(3)
        except NoSuchElementException:
            posting_num += 1
            driver.find_element(by=By.LINK_TEXT, value=f'{jobs_available[posting_num]}').click()
            time.sleep(2)
            driver.find_element(by=By.CLASS_NAME, value="jobs-s-apply").click()
        finally:
            # Complete application
            jobs_available.remove(jobs_available[posting_num])
            try:
            # Wait and click "Apply" button
                time.sleep(2)
                phone_num = driver.find_element(by=By.CLASS_NAME, value='fb-single-line-text__input')
                phone_num.clear()
                time.sleep(2)
                phone_num.send_keys(MY_PHONE_NUMBER)
                time.sleep(2)
                driver.find_element(by=By.CSS_SELECTOR, value='footer button').click()
                time.sleep(2)
                driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Review your application"]').click()
                time.sleep(2)
                driver.find_element(by=By.CSS_SELECTOR, value='[aria-label="Submit application"]').click()
            except NoSuchElementException:
                print('Cannot apply, skipped')
            except (NoSuchElementException, ElementClickInterceptedException):
                print(f"Skipping '{jobs_available[posting_num]}' due to error.")
                continue
    print("Application process complete.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    driver.quit()
