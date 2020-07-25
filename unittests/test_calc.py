import unittest
from unittests import calc


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ will run once before all test"""
        pass

    @classmethod
    def tearDownClass(cls):
        """ will run once after all tests"""
        pass

    def setUp(self):
        """ will be run before each test_foo"""
        self.bar = 0
        pass

    def tearDown(self):
        pass


    def test_add(self):
        """ test_foo is the std naming scheme"""
        self.assertEqual(calc.add(10, 5), 15)


    def test_divide(self):

        self.assertEqual(calc.divide(4,2),2)

        # Bad form.
        # self.assertRaises(ValueError, calc.divide,10 , 0)
        # Good form.
        with self.assertRaises(ValueError):
            calc.divide(10,self.bar)


# usually run as 'python -m unittest test_calc.py'

if __name__ == '__main__':
    unittest.main()


# test should be isolated
# any thest should be able to run independent of otehr tests

# test driven development: write test first, then the code