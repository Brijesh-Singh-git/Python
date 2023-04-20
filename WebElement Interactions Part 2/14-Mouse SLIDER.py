import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
time.sleep(2)

min_slider = driver.find_element_by_xpath("//span[1]")
max_slider = driver.find_element_by_xpath("//span[2]")

print("Location of Silders before MOVING------------------>>>")
print(min_slider.location)  # {'x': 59, 'y': 250}
print(max_slider.location)  # {'x': 545, 'y': 250}

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider, 102,0).perform()
act.drag_and_drop_by_offset(max_slider, -120,0).perform()

print("Location of Silders after MOVING ------------------>>>")
print(min_slider.location)
print(max_slider.location)
