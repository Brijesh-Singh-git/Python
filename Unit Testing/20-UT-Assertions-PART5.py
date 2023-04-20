import  unittest

class Test_Cases(unittest.TestCase):
    def test_Name(self):

        self.assertGreater(100, 10)
       # self.assertGreaterEqual(100,100)
       # self.assertLess(10,100)
       # self.assertLessEqual(100,100)



    if __name__ == "__main__":
        unittest.main()