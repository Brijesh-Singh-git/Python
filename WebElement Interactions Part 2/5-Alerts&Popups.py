import time

from selenium import webdriver

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

# driver.get("https://demo.automationtesting.in/Alerts.html")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element_by_xpath("//button[@class='btn btn-danger']").click()
# time.sleep(2)
#
# # driver.switch_to.alert.accept()  # It will close this by clicking Ok button
#
# driver.switch_to.alert.dismiss()


driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

driver.find_element_by_xpath("//button[@class='btn btn-info']").click()
time.sleep(2)

driver.switch_to.alert.sendKeys("Hello this is ok")
