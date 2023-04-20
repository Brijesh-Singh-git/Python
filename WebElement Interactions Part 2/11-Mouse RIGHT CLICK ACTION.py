import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(2)

button = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(button).perform()   # RIGHT CLICK OPERATION

time.sleep(4)
