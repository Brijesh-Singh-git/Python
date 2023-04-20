# Import the service class
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")

driver.find_element(By.XPATH, " //input[@id='Password']").clear()
driver.find_element(By.XPATH, " //input[@id='Password']").send_keys("admin")

driver.implicitly_wait(2)

driver.find_element(By.XPATH,"//button[@type='submit']").click()