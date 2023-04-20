import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver import ActionChains


class Test(unittest.TestCase):
    aut = "https://demo.automationtesting.in/Windows.html"

    def setUp(self):
        self.driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        self.driver.get(self.aut)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)


    def tearDown(self):
        self.driver.close()


    def test_MouseActions(self):

        a =self.driver.find_element_by_xpath("//a[normalize-space()='SwitchTo']")
        b= self.driver.find_element_by_xpath("//a[normalize-space()='Windows']")
        c = self.driver.find_element_by_xpath("//a[normalize-space()='Frames']")
        print(c)

        #MOUSE ACTIONS  -----> # MOUSE HOVER
        act = ActionChains(self.driver)   # Selenium Package for Mouse operations
        time.sleep(3)
        var = act.move_to_element(a).move_to_element(b).click(c).perform
        time.sleep(5)

