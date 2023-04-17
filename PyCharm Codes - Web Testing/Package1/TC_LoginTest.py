import  unittest

class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("This is login by Facebbok test")
        self.assertTrue(True)

    def test_loginByTwitter(self):
        print("This is login by Twitter test")
        self.assertTrue(True)


    if __name__ == "__main__":
        unittest.main()