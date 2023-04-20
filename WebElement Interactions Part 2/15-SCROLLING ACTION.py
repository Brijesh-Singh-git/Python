import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(2)

# SCROLLING


# Approach 1

# driver.execute_script("window.scrollBy(0,2500)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("No of Pixels moves: ", value)


# Approach 2 ---> Based on Element

# flag = driver.find_element_by_xpath("//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("No of Pixels moves: ", value)

# Approach 3 -----> Scroll till the end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


# Approach 4 -----> Scroll up  to the page
time.sleep(3)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")