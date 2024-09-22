import unittest

from ..src.Assignment2.util import score

class MyTestCase(unittest.TestCase):

    def test_something(self):
        scores = [6, 8, 9, 4, 2, 10]
        self.assertEqual(score(scores), 9)  # add assertion here

if __name__ == '__main__':
    unittest.main()
