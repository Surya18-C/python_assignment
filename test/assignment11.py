import unittest

from ..src.Assignment11.utill import validation

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(validation(), ['rex@mail.com'])  # add assertion here


if __name__ == '__main__':
    unittest.main()
