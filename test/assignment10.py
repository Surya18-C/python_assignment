import unittest

from ..src.Assignment10.utill import cnt

class MyTestCase(unittest.TestCase):
    def test_something(self):
        val=["apple","apple","banana"]
        self.assertEqual(cnt(val),[2,1])  # add assertion here


if __name__ == '__main__':
    unittest.main()
