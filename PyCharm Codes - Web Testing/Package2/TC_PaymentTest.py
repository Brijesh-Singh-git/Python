import  unittest

class paymentTest(unittest.TestCase):

    def test_paymentInDollar(self):
        print("This is payment in Dollar Test")
        self.assertTrue(True)

    def test_paymentInRupees(self):
        print("This is payment in Rupees Test")
        self.assertTrue(True)

if __name__ =="__main__":
    unittest.main()
