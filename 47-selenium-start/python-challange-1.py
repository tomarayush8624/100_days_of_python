from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/ayush/MEGAsync/chromeDriver/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.python.org/")
menu = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li")

upcoming_events = {
    0: {},
    1: {},
    2: {},
    3: {},
    4: {}}
for i in range(0, len(menu)):
    date = (menu[i].find_element(By.TAG_NAME, "time").text)
    time = (menu[i].find_element(By.TAG_NAME, "a").text)

    upcoming_events[i]["date"] = date
    upcoming_events[i]["time"] = time

print(upcoming_events)

driver.quit()
