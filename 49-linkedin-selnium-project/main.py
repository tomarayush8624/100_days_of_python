import os
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import  Options
import time

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
# print(password)

options = Options()
options.add_experimental_option("detach", True)
chrome_driver_path = "/home/ayush/MEGAsync/chromeDriver/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London"
           "%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
driver.find_element(By.CLASS_NAME, "nav__button-secondary").click()
time.sleep(5)
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CLASS_NAME, "btn__primary--large").click()


