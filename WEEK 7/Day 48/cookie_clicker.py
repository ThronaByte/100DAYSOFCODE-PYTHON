from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

chrome_driver_path = 'C:/Development/chrome-win32/chromedriver-win32/chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Wait for the cookie element to load
cookie = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, "cookie"))
)

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

def get_cookie_count():
    """Retrieve the current number of cookies available for spending."""
    money_element = driver.find_element(By.ID, "money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")
    return int(money_element)

def get_affordable_upgrades(cookie_upgrades):
    """Return a dictionary of affordable upgrades based on the current cookie count."""
    cookie_count = get_cookie_count()
    affordable = {cost: upgrade_id for cost, upgrade_id in cookie_upgrades.items() if cookie_count >= cost}
    return affordable

def purchase_upgrade():
    """Buy the most expensive affordable upgrade to maximize CPS."""
    all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    item_prices = []
    for price in all_prices:
        element_text = price.text
        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    cookie_upgrades = {item_prices[i]: item_ids[i] for i in range(len(item_prices))}

    affordable_upgrades = get_affordable_upgrades(cookie_upgrades)
    if affordable_upgrades:
        highest_price_upgrade = max(affordable_upgrades)
        upgrade_id = affordable_upgrades[highest_price_upgrade]
        driver.find_element(By.ID, upgrade_id).click()
        print(f"Purchased upgrade: {upgrade_id} costing {highest_price_upgrade} cookies.")

while True:
    cookie.click()

    if time.time() > timeout:
        purchase_upgrade()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print("Cookies per second:", cookie_per_s)
        break

driver.quit()
