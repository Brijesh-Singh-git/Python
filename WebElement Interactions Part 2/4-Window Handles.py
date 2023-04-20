import time

from selenium import  webdriver

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//a[@href='http://www.selenium.dev']/button").click()
print(driver.current_window_handle)  # DB7301C398268354047BDED3B96E2E73 ---->Parent Window
time.sleep(2)
# To get window handles of each and every windows

windowHandles = driver.window_handles

for handle in windowHandles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()
time.sleep(2)
driver.quit()