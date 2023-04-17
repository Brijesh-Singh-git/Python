import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentReturnTest import payementReturnsTest
from Package2.TC_PaymentTest import paymentTest

# Get all the tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(paymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(payementReturnsTest)

# Sanity Test Suite ----> It will contain only Login Functionality
sanityTestSuite = unittest.TestSuite([tc1, tc2])

# Functional Test Suites
functionalSUite = unittest.TestSuite([tc3,tc4])

# Master Test Suite -----> It will run all the test

masterTest = unittest.TestSuite([tc1,tc2,tc3,tc4])

unittest.TextTestRunner().run(masterTest)  # Command to run the Test Suite
