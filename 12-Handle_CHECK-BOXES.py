import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# Select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# Select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# Approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# Approach 2
# for checkbox in checkboxes:
#     checkbox.click()


# Approach 3
# Select multiple checkboxes based on choice
# for checkbox in checkboxes:
#     weekName = checkbox.get_attribute('id')
#     if weekName == 'monday' or weekName == 'sunday':
#         checkbox.click()


# Approach 4
# Select last 3 checkboxes
# range(5,7) ---> 5, 6,7

# for i in range(len(checkboxes)-3, len(checkboxes)):
#     checkboxes[i].click()
#

# Approach 5
# Select first 3 checkboxes

# for i in range(len(checkboxes)):
#     if i<2:
#      checkboxes[i].click()


# Approach 6
# Clearing all the checkboxes

time.sleep(3)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.clear()
