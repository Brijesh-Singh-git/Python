import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(2)
a =driver.find_element_by_xpath("//a[normalize-space()='SwitchTo']")
b= driver.find_element_by_xpath("//a[normalize-space()='Windows']")
c = driver.find_element_by_xpath("//a[normalize-space()='Frames']")

act = ActionChains(driver)   # Selenium Package for Mouse operations
time.sleep(3)

#MOUSE HOVER
act.move_to_element(a).move_to_element(b).click(c).perform
time.sleep(5)

