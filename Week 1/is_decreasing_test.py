import unittest

from is_decreasing import is_decreasing


class Is_decreasing_test(unittest.TestCase):

    def test_is_decreasing(self):
        self.assertTrue(is_decreasing([5, 4, 3, 2, 1]))
        self.assertFalse(is_decreasing([1, 2, 3]))
        self.assertTrue(is_decreasing([100, 50, 20]))
        self.assertFalse(is_decreasing([1, 1, 1, 1]))

if __name__ == '__main__':
    unittest.main()
