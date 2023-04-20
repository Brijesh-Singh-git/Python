import unittest
from selenium import webdriver
from xlsxwriter import worksheet
import xlwt


class Test(unittest.TestCase):
    application_under_test = "https://testautomationpractice.blogspot.com/"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        self.driver.get(self.application_under_test);
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.close()

    def testName(self):
        table = self.driver.find_element_by_xpath("//table[@name='BookTable']")
        rows = table.find_elements_by_tag_name("tr")

        book = xlwt.Workbook()
        sheet = book.add_sheet("OfferDetils", False)

        for i in range(1, len(rows)):
            col = rows[i].find_elements_by_tag_name("td")
            for j in range(0, len(col)):
                print(i)
                if (j == 1):
                    offer_details = col[j].text
                    sheet.write(i, 0, offer_details)
                elif (j == 2):
                    coupon = col[j].text
                    sheet.write(i, 1, coupon)
                else:
                    continue

        book.save("Offers.xls")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
