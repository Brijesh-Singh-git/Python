import time

from selenium import webdriver

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(2)
driver.switch_to.default_content()  # This will take to the main page
driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("//ul[@title='Interfaces']/li[13]/a").click()
time.sleep(2)
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("//div[@class='topNav']//a[normalize-space()='Help']").click()

