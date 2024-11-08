from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe'

chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get('https://www.python.org/')

event_time = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')


events = {}
for event in range(len(event_time)):
    events[event] = {
        "time": event_time[event].text,
        "name": event_name[event].text,
    }
pprint(events)

driver.close()
driver.quit()
