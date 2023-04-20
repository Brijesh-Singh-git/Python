import  unittest

class SignupTest(unittest.TestCase):
    def test_signupByEmail(self):
        print("This is signup by email test")
        self.assertTrue(True)

    def test_signupByFacebook(self):
        print("This is signup by Facebbok test")
        self.assertTrue(True)

    def test_signupByTwitter(self):
        print("This is signup by Twitter test")
        self.assertTrue(True)


    if __name__ == "__main__":
        unittest.main()