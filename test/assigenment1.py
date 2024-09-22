import unittest

from python_assignment.src.Assignment1.util import average

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertGreater(average(), 10.0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
