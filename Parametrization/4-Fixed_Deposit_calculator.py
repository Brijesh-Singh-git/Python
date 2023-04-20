import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

from Parametrization import XL_Utils

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
driver.implicitly_wait(5)

file = "G:\INFOSYS Lectures & Codes\Python Testing Codes\Python Codes\Fixed_Deposit_data.xlsx"

rows =XL_Utils.getRowCount(file, "Sheet1")

for r in range(2,rows+1):
    #Reading Data from Excel
    princ = XL_Utils.readData(file,"Sheet1",r,1)
    roi = XL_Utils.readData(file,"Sheet1",r,2)
    period1 = XL_Utils.readData(file,"Sheet1",r,3)
    period2 = XL_Utils.readData(file,"Sheet1",r,4)
    fre = XL_Utils.readData(file,"Sheet1",r,5)
    exp_mat = XL_Utils.readData(file,"Sheet1",r,6)  # It will capture in String
    # Now pass this data to the Application
    driver.find_element_by_xpath("//input[@id='principal']").send_keys(princ)
    driver.find_element_by_xpath("//input[@id='interest']").send_keys(roi)
    driver.find_element_by_xpath("//input[@id='tenure']").send_keys(period1)
    perioddrp = Select(driver.find_element_by_xpath("//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(period2)

    frequency = Select(driver.find_element_by_xpath("//select[@id='frequency']"))
    frequency.select_by_visible_text(fre)

    driver.find_element_by_xpath("//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    actual_matu = driver.find_element_by_xpath("//span[@id='resp_matval']/strong").text

    #Validation
    if float(exp_mat)== float(actual_matu):
        print("Test Passed")

        # Now to write this data into Excel
        XL_Utils.writeData(file, "Sheet1",r , 8 , "Passed")
        XL_Utils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed!!")

        # Now to write this data into Excel
        XL_Utils.writeData(file, "Sheet1", r, 8, "Failed")
        XL_Utils.fillRedColor(file, "Sheet1", r, 8)

    # Before entering new data we need to clear the input fields in our application
    driver.find_element_by_xpath("//img[@class='PL5']").click()
    time.sleep(2)

driver.close()


