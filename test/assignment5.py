import unittest

from ..src.Assignment5.util import str_format

class MyTestCase(unittest.TestCase):
    def test_something(self):
        n=5
        self.assertEqual(str_format(n), ['1 1 1 1', '2 2 2 10', '3 3 3 11', '4 4 4 100', '5 5 5 101'])  # add assertion here


if __name__ == '__main__':
    unittest.main()
