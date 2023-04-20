from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Create Service class Object
serv_obj = Service("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) Count number of Rows and Columns

noOfrows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
print("No of Rows are : ", noOfrows)

nofOfcolumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))
print("No of Columns are: ", nofOfcolumns)

print("-----------------------------------------------------------------------")
# 2) Read specific row and column data

# a = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text
# print(a)
#
# b = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[3]/td[3]").text
# print(b)

print("-----------------------------------------------------------------------")

# 3) Read all the rows & column data
"""
print("------------Printing all the rows and columns --------------------------")

for r in range(2, noOfrows + 1):
    for c in range(1, nofOfcolumns + 1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(data, end=" ")
        print()
        
        """
print("------------------Read data based on condition----------------------------------------")
# 4) Read data based on condition

for r in range(2, noOfrows + 1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text

    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName, "             ", authorName, "             " , price)

driver.close()
