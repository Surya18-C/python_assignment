import unittest

from ..src.Assignment3.util import mutation

class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected_out="ApplA"
        self.assertEqual(mutation(), expected_out)  # add assertion here


if __name__ == '__main__':
    unittest.main()
