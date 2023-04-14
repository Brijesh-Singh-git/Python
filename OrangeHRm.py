from selenium import webdriver 

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://www.google.com")


driver.find_element_by_name("btnK").click()

driver.implicitly_wait(5)

driver.close()


