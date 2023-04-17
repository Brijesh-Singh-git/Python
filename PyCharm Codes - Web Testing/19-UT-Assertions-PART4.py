import  unittest

class Test_Cases(unittest.TestCase):
    def test_Name(self):
        list = {"python", "java" ,"javascript"}

        # self.assertIn("python",list)  #passed
        # self.assertIn("ruby",list)   # failed as RUBY is not in list

        #self.assertNotIn("python" ,list)  #failed as python is present
        self.assertNotIn("ruby" ,list)  #passed as ruby is not present

    if __name__ =="__main":
        unittest.main()

