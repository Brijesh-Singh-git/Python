import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

myWait = WebDriverWait(driver, 10, ignored_exceptions=[Exception]) #-----> Explicit wait declaration

driver.get("https://www.google.com")
driver.maximize_window()

driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("Selenium")
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").submit()

searchLink = myWait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium']")))
searchLink.click()