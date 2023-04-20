import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame("iframeResult")

driver.find_element_by_xpath("/html/body/input[1]").clear()
driver.find_element_by_xpath("/html/body/input[1]").send_keys("HELLO this is nice")
time.sleep(2)
doubleClick = driver.find_element_by_xpath("//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(doubleClick).perform()

