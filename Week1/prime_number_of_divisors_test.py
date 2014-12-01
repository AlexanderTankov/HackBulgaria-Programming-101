import unittest

from prime_number_of_divisors import prime_number_of_divisors


class Prime_number_of_divisors_test(unittest.TestCase):

    def test_prime_number_of_divisors(self):
        self.assertTrue(prime_number_of_divisors(7))
        self.assertFalse(prime_number_of_divisors(8))
        self.assertTrue(prime_number_of_divisors(9))

if __name__ == '__main__':
    unittest.main()
