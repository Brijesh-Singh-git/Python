import time

from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
class Test_HRM:

    @allure.severity(allure.severity_level.CRITICAL)
    def test_logo(self):
        self.driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        status = self.driver.find_element_by_xpath("//img[@alt='company-branding']").is_displayed()
        if status == True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Logo_Screen",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_list_Employees(self):
        pytest.skip("Skipping this test!!!!")

    @allure.severity(allure.severity_level.MINOR)
    def test_login(self):
        self.driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        act_title = self.driver.title

        if act_title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
