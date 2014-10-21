import unittest

from nan_expand import nan_expand


class Nan_expand_test(unittest.TestCase):

    def test_nan_expand(self):
        self.assertEqual(nan_expand(0), "")
        self.assertEqual(nan_expand(1), "Not a NaN")
        self.assertEqual(nan_expand(2), "Not a Not a NaN")
        self.assertEqual(nan_expand(3), "Not a Not a Not a NaN")


if __name__ == '__main__':
    unittest.main()
