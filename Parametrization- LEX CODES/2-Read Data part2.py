import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import  webdriver
import  xlrd
import  time

serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)

WorkBook = xlrd.open_workbook("G:\INFOSYS Lectures & Codes\Python Testing Codes\Python Codes\Credientials.xlsx")
WorkSheet = WorkBook.sheet_names("Sheet1")
RowCount = WorkSheet.nrows

for r in range(1, RowCount):
    Username = WorkSheet.cell_value(r, 1)
    Password = WorkSheet.cell_value(r, 1)

    driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(Username)

    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(Password)