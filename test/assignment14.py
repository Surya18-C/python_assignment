import unittest

from ..src.Assignment14.utill import unique_element

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(unique_element(),[1, 2, 4, 3, 5, 6] )  # add assertion here


if __name__ == '__main__':
    unittest.main()
