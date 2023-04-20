import  unittest
from selenium import  webdriver

class Test_Cases(unittest.TestCase):
    def test_Name(self):
        driver=webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        # driver = None

        self.assertIsNotNone(driver) # IT will pass as drive is having value

        # self.assertIsNone(driver)  # It will get failed as the driver is having value


    if __name__ == "__main__":
        unittest.main()