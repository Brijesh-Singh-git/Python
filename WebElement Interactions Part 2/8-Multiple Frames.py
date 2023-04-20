import time
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    aut = "https://demo.automationtesting.in/Frames.html"

    def setUp(self):
        self.driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        self.driver.get(self.aut)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)


    def tearDown(self):
        self.driver.close()


    def test_frames(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Iframe with in an Iframe']").click()
        time.sleep(2)
        outerFrame = self.driver.find_element_by_xpath("//iframe[@src='MultipleFrames.html']")
        self.driver.switch_to.frame(outerFrame)
        time.sleep(2)
        innerFrame = self.driver.find_element_by_xpath("/html/body/section/div/div/iframe")
        self.driver.switch_to.frame(innerFrame)
        # time.sleep(2)
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("HELLO WELCOME TO PAGE")

        self.driver.switch_to.parent_frame()  # directly it will switch to the parent frame in SELENIUM 4
        time.sleep(2)