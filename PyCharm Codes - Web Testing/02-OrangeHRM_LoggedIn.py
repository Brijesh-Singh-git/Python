from selenium import webdriver
from selenium.webdriver.common.by import By



# SELENIUM 4 CODE

#Import the service class
from selenium.webdriver.chrome.service import Service

#Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.implicitly_wait(2)

driver.find_element(By.NAME, "password").send_keys("admin123")
driver.implicitly_wait(2)

title=driver.title
print("The Title of the Page before login : " + title)

driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
driver.implicitly_wait(2)

title2=driver.title
print("The Title of the Page before login : " + title2)

driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
driver.implicitly_wait(2)

actualTitle = driver.title
exp_title = "OrangeHRM"

if actualTitle == exp_title:
    print("TEST CASE PASSSED")
else:
    print("TEST CASE FAILED")

    driver.close()








"""

#SELENIUM 3 CODE
driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_name("username").send_keys("Admin")
driver.implicitly_wait(2)

driver.find_element_by_name("password").send_keys("admin123")
driver.implicitly_wait(2)

title=driver.title
print("The Title of the Page before login : " + title)

driver.find_element_by_class_name("orangehrm-login-button").click()
driver.implicitly_wait(2)
title2=driver.title
print("The Title of the Page before login : " + title2)

driver.find_element_by_class_name("oxd-userdropdown-tab").click()
driver.implicitly_wait(2)

actualTitle = driver.title
exp_title = "OrangeHRM"

if actualTitle == exp_title:
    print("TEST CASE PASSSED")
else:
    print("TEST CASE FAILED")

    driver.close()
    
    
    """