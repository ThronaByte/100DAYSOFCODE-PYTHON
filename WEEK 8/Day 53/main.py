from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from time import sleep

# Load environment variable
load_dotenv(".env")
ZILLOW_CLONE_URL = os.getenv("ZILLOW_CLONE_URL")
GOOGLE_FORMS = os.getenv("GOOGLE_FORMS")

service = Service("C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

param = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 "
                  "Safari/537.36 Edg/130.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(ZILLOW_CLONE_URL, headers=param)
soup = BeautifulSoup(response.text, "html.parser")


def get_links():
    """Function to extract links from Zillow Clone"""
    all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
    all_links = ["https://www.zillow.com" + link["href"] if not link["href"].startswith("http") else link["href"] for
                 link in all_link_elements]
    print(f"There are {len(all_links)} links to individual listings in total:\n")
    print(all_links)
    return all_links


def get_addresses():
    """Function to extract addresses from Zillow Clone"""
    all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
    all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
    print(f"\nCleaned up addresses ({len(all_addresses)}):\n")
    print(all_addresses)
    return all_addresses


def get_prices():
    """Function to extract prices from Zillow Clone"""
    all_price_elements = soup.select(".PropertyCardWrapper span")
    all_prices = [price.get_text().replace("/mo", "").split("+")[0].strip() for price in all_price_elements
                  if "$" in price.text]
    print(f"\nCleaned up prices ({len(all_prices)}):\n")
    print(all_prices)
    return all_prices


# Gather data from Zillow Clone
all_links = get_links()
all_addresses = get_addresses()
all_prices = get_prices()


def submit_form_data(address, price, link):
    """Submit each listing to Google Form"""
    driver.get(f"{GOOGLE_FORMS}")
    sleep(2)

    # Fill in Google Form fields using XPaths
    address_field = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div'
                                        '/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                      '/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]'
                                     '/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    # Populate fields with data
    address_field.send_keys(address)
    price_field.send_keys(price)
    link_field.send_keys(link)
    submit_button.click()
    sleep(2)

# Loop through data and submit to Google Forms
for i in range(len(all_links)):
    submit_form_data(all_addresses[i], all_prices[i], all_links[i])

driver.quit()
