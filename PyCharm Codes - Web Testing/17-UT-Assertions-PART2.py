import  unittest
from selenium import  webdriver

class Test_Cases(unittest.TestCase):
    def test_Name(self):
        driver=webdriver.Chrome("G:\INFOSYS Lectures & Codes\Stream Training\JAR Files\CD.exe")
        driver.get("https://www.google.com")

        title = driver.title

        #assertTrue
        # self.assertTrue(title == "Google")  #True

        # assertFalse
        self.assertFalse(title == "Googl22e")  #True

    if __name__ == "__main__":
     unittest.main()