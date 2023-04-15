import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://demo.nopcommerce.com")
driver.get("https://amazon.in")
driver.get("https://flipkart.com")

driver.maximize_window()
time.sleep(5)
driver.back()    #----> THis will go to amazon page
time.sleep(5)
driver.forward()  #---> this will go to flipkart

time.sleep(5)

driver.quit()