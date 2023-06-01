from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/ayush/MEGAsync/chromeDriver/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# total_articles = driver.find_element(By.ID, "articlecount")
# print(total_articles.find_element(By.TAG_NAME, "a").text)

total_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(total_articles.text)
total_articles.click()