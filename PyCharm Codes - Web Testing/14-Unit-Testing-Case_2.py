import unittest
from selenium import webdriver


class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        self.driver.get("https://www.google.com")
        print("Title of the page is : ", self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        self.driver.get("https://www.bing.com")
        print("Title of the page is : ", self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
