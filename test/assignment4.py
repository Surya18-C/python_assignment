import unittest

from ..src.Assignment4.util import split_remove_duplicates

class MyTestCase(unittest.TestCase):
    def test_something(self):

        self.assertEqual(split_remove_duplicates("AALLEE",2), ["AA","LL","EE"])  # add assertion here


if __name__ == '__main__':
    unittest.main()
