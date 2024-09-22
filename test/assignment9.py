import unittest

import numpy as np

from  ..src.Assignment9.util import float_format

class MyTestCase(unittest.TestCase):
    def test_something(self):
        np.testing.assertEqual(float_format(1.2, 2.2, 3.2, 4.2) , "(([6., 5., 4.]) , ([5., 4., 3.]), ([6., 4., 3.]))")  # add assertion here


if __name__ == '__main__':
    unittest.main()
