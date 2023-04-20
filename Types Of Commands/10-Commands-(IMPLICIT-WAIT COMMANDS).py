import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.google.com")

driver.maximize_window()

driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("Selenium")
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").submit()

# time.sleep(5)

driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//h3[normalize-space()='Selenium']").click()