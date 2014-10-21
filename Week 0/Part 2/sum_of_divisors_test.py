import unittest

from sum_of_divisors import sum_of_divisors


class Sum_of_divisors_test(unittest.TestCase):

    def test_sum_of_divisors(self):
        self.assertEqual(sum_of_divisors(8), 15)
        self.assertEqual(sum_of_divisors(7), 8)
        self.assertEqual(sum_of_divisors(1), 1)
        self.assertEqual(sum_of_divisors(1000), 2340)

if __name__ == '__main__':
    unittest.main()
