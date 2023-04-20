from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(5)
driver.find_element_by_name("username").send_keys("Admin")
driver.implicitly_wait(2)
driver.find_element_by_name("password").send_keys("admin123")
driver.implicitly_wait(2)
driver.find_element_by_class_name("orangehrm-login-button").click()



