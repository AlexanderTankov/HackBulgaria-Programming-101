import unittest

from is_prime import is_prime


class Is_prime_test(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(8))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(-10))

if __name__ == '__main__':
    unittest.main()
