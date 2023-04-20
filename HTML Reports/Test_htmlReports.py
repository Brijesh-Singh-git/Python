import time

from selenium import webdriver
import unittest
import HtmlTestRunner


# ORANGE HRM login Test

class HRM_Login_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_HomePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        title_page = self.driver.title
        self.assertEqual("OrangeHRM", title_page, "Web Page title is matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.assertEqual("OrangeHRM", self.driver.title, "Web Page title is matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("TEST COMPLETED")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
                                                        "G:\\INFOSYS Lectures & Codes\\Python Testing Codes\\Python Codes\\HTML Reports\\Reports"))
