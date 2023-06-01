from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


chrome_driver_path = "/home/ayush/MEGAsync/chromeDriver/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.python.org/")
# price = driver.find_element_by_id("price_dsfsd")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element(By.CLASS_NAME, "python-logo")

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, 'i dont care bro')

driver.quit()