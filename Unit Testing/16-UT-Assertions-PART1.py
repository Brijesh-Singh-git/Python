import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def test_Name(self):
        driver = webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        driver.get("https://www.google.com")
        titleOfWebpage = driver.title

        # assertEqual
        # self.assertEqual("Google", titleOfWebpage, "Webpage Title is not same")

        #assertNotEquals
        self.assertNotEquals("Google12", titleOfWebpage)

    if __name__ == "__main__":
        unittest.main()
