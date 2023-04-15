from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

# driver.get("https://demo.nopcommerce.com")
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

driver.maximize_window()

# searchBox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# print("Display Status: " , searchBox.is_displayed())
# print("Enabled Status: ", searchBox.is_enabled())


#is_selected --------> Only for Radio Button and CHeckboxes

radioButton = driver.find_element(By.XPATH,"//input[@id='gender-male']")
print("Radio Button Selected or not: " , radioButton.is_selected())
driver.implicitly_wait(4)
radioButton_Selected = driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
print("Radio Button Selected or not: " , radioButton.is_selected())

driver.implicitly_wait(4)
driver.quit()