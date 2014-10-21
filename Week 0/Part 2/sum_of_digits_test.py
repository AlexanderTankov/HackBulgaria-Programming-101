import unittest

from sum_of_digits import sum_of_digits


class Sum_of_digits_test(unittest.TestCase):

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(1325132435356), 43)
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(6), 6)
        self.assertEqual(sum_of_digits(-10), 1)

if __name__ == '__main__':
    unittest.main()
