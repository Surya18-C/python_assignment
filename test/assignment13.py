import unittest

from ..src.Assignment13.utill import min_max

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(min_max(), 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
