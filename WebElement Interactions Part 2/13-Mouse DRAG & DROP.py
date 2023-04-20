import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(2)

rome = driver.find_element_by_id("box6")
italy = driver.find_element_by_id("box106")

oslo = driver.find_element_by_id("box1")
norway = driver.find_element_by_id("box101")

seol = driver.find_element_by_id("box5")
korea = driver.find_element_by_id("box106")

wash = driver.find_element_by_id("box3")
usa = driver.find_element_by_id("box103")

madrid = driver.find_element_by_id("box7")
spain = driver.find_element_by_id("box107")


act = ActionChains(driver)
# time.sleep(2)

act.drag_and_drop(rome,italy).perform()
act.drag_and_drop(wash,usa).perform()
act.drag_and_drop(madrid,spain).perform()
act.drag_and_drop(oslo,norway).perform()