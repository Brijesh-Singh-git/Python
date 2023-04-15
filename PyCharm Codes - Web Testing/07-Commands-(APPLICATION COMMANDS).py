
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

#APPLICATION COMMANDS
page = driver.page_source
print("The page source of current webPage is:\n   " , page)

title = driver.title
print("The page title of current webPage is:   " , title)

print("The current URL of the page is: " , driver.current_url)


driver.quit()