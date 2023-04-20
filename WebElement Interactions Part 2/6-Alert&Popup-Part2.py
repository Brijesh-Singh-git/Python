import time

from selenium import webdriver

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(2)

# ------------------------------------- ALERTS--------------------------------
# Open alert Window
# driver.find_element_by_xpath("//button[@onclick='jsAlert()']").click()
# driver.find_element_by_xpath("//button[@onclick='jsPrompt()']").click()
# time.sleep(2)
#
# alertWindow = driver.switch_to.alert
#
# print(alertWindow.text)
# alertWindow.send_keys("Hello")
# time.sleep(2)
# # alertWindow.accept()
# alertWindow.dismiss()


# ------------------------------------AUTHENTICATION POPUPS-----------------------------------

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

