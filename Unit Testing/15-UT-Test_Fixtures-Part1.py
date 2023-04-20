import unittest


# Module in python: In simple words, module is a file consisting of Python code with .py extension. It can contain functions, classes, and variables.
# Additionally, it can have plain runnable code as well.

# def setUpModule(): # will be executed before any class or nay method present in the test class
#        print("SetUpModule")
#
# def tearDownModule(): # will be executed after completing everything present in the python module
#        print("TearDownModule")


def setUpModule():
    print("In setUpModule")
def tearDownModule():
    print("In tearDownModule")

class AppTesting(unittest.TestCase):

    @classmethod  # Decorator
    def setUp(self):  # This setup method will run every time before the execution of the new Test method
        print("This is a Setup Method")

    @classmethod
    def tearDown(self):  # This tearDown method will run every time after the execution of the new Test method
        print("This is a Teardown Method")

    @classmethod
    def setUpClass(cls):  # Executes once when the class is started
        print("This is a Setup Class")

    @classmethod
    def tearDownClass(cls):  # Executes once after the class is completed
        print("This is a TearDown Class")

    def test_Search(selfe):
        print("This is a search Test")

    def test_AdvancedSearch(self):
        print("This is an Advnaced Search test")

    def test_prepaidRecharge(self):
        print("This is a Prepaid Recharge")

    def test_postpaidRecharge(self):
        print("This is a PostPaid Recharge")


if __name__ == '__main__':
    unittest.main()
