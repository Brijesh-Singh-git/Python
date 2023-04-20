import unittest
from selenium import  webdriver
import  xlrd
import  time

class Test(unittest.TestCase):
    
    aut = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def setUp(self):
        self.driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        self.driver.get(self.aut)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def tearDown(self):
        self.driver.close()

    def test_Login(self):
        WorkBook = xlrd.open_workbook("G:\INFOSYS Lectures & Codes\Python Testing Codes\Python Codes\Credientials.xlsx")
        WorkSheet = WorkBook.sheet_by_index(0)
        RowCount = WorkSheet.nrows

        for r in range(1, RowCount):
            Username = WorkSheet.cell_value(r,1)
            Password = WorkSheet.cell_value(r,1)

            self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(Username)

            self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(Password)


            self.driver.find_element_by_xpath("//button[@type='submit']").click()

            time.sleep(3)


if __name__ =="__main__":
    unittest.main()