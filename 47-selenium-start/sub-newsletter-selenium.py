from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/home/ayush/MEGAsync/chromeDriver/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://changelog.com/news")
email_form = driver.find_element(By.CLASS_NAME, "signup-form-input")
email_form.send_keys("klubaih@internetkeno.com")
signup_btn = driver.find_element(By.CLASS_NAME, "signup-form-submit-button").click()
# signup_btn.send_keys(Keys.ENTER)