import unittest

from ..src.Assignment15.utill import count

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(count(), ('Total words', 6, 'Total letters', 30))  # add assertion here


if __name__ == '__main__':
    unittest.main()
