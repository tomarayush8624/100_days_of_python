from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import time
from datetime import datetime

# import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path = "/home/ayush/MEGAsync/chromeDriver/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

exit_time = time.time() + 50 * 60
prices = {}
store = driver.find_element(By.ID, "store")
store_items = store.text.split("\n")
ele = []
for i in range(0, len(store_items), 2):
    ele.append(store_items[i].split(" - "))
for i in range(0, len(ele)):
    prices[i] = {
        "id": f"buy{ele[i][0]}",
        "price": int(ele[i][1].replace(',', '')),
    }
# print(prices)

while time.time() < exit_time:
    if datetime.now().second % 5 == 0:
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        for i in range(7, -1, -1):
            if money > prices[i]["price"]:
                print(prices[i]['id'])
                driver.find_element(By.ID, f"{prices[i]['id']}").click()
                time.sleep(.5)
    cookie.click()

print(driver.find_element(By.ID, "money").text)
