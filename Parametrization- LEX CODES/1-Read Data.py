import time

import xlrd
from selenium import webdriver

driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)

user1 = driver.find_element_by_xpath("//input[@placeholder='Username']")
pass1 = driver.find_element_by_xpath("//input[@placeholder='Password']")


workbook = xlrd.open_workbook("OrangeHRM.xlsx")
sheet = workbook.sheet_by_name("Sheet1")

# get total no of rows
rowCount = sheet.nrows
colsCount = sheet.ncols
print(rowCount)
print(colsCount)

#Read data

for r in range(1,rowCount+1):
    user_name = sheet.cell_value(r,0)
    pass_word = sheet.cell_value(r,1)

    user1.send_keys(user_name)
    time.sleep(2)
    pass1.send_keys(pass_word)
    time.sleep(2)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5)

time.sleep(4)
