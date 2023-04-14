#Import the service class
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://amazon.in")

driver.maximize_window()


#By CLASS_NAME & TAG_NAME
sliders = driver.find_elements(By.CLASS_NAME, "copilot-secure-display")
print("No of classes with this name is: ",len(sliders))

anchor_tags = driver.find_elements(By.TAG_NAME, "a")
print("Nof of anchor tags present on Amazon.in is: ", len(anchor_tags) )


