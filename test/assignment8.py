import datetime
import unittest

from ..src.Assignment8.util import delta

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(delta(), datetime.timedelta(seconds=7200))  # add assertion here


if __name__ == '__main__':
    unittest.main()
