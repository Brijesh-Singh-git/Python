import time
import  unittest
import HtmlTestRunner
from selenium import  webdriver

import sys
sys.path.append("G:\INFOSYS Lectures & Codes\Python Testing Codes\POM Based Project")

from Page_Objects.Login_page import loginPage

class Login_Test(unittest.TestCase):

    URL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome("..\\Drivers\\CD.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.URL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = loginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)

        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title, "Wepage title is not Matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\Reports"))