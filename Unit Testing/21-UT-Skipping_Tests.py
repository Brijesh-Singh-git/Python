import unittest
class AppTesting(unittest.TestCase):

    @unittest.SkipTest  # Decorator for skipping the particular test method
    def test_search(self):
        print("This is a search test 1")

    def test_search2(self):
        print("This is a search test 2")

    @unittest.skipIf(1==5, "Skipping the method 3 as 1==1") # now it wont skipp as 1==5 ....change 1==1 and it will skip this test case
    def test_search3(self):
        print("This is a search test 3")

    def test_search4(self):
        print("This is a search test 4")

    @unittest.skip("I am skipping this test method 5")
    def test_search5(self):
        print("This is a search test 5")


    if __name__ == "__main__":
        unittest.main()



