import unittest

from ..src.Assignment6.util import calender_module

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calender_module("18 05 2003"), "Sunday")  # add assertion here
        self.assertEqual(calender_module("15 09 2003"), "Monday")

if __name__ == '__main__':
    unittest.main()
