import unittest

from prime_factorization import prime_factorization, repetition_in_list


class Prime_factorization_test(unittest.TestCase):
    def test_repetition_in_list(self):
        self.assertEqual(repetition_in_list([2, 2, 2]), [(2, 3)])
        self.assertEqual(repetition_in_list([1, 2, 3]), [(1, 1), (2, 1), (3, 1)])
        self.assertEqual(repetition_in_list([]), [])

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(10), [(2, 1), (5, 1)])
        self.assertEqual(prime_factorization(14), [(2, 1), (7, 1)])
        self.assertEqual(prime_factorization(356), [(2, 2), (89, 1)])
        self.assertEqual(prime_factorization(89), [(89, 1)])
        self.assertEqual(prime_factorization(1000), [(2, 3), (5, 3)])


if __name__ == '__main__':
    unittest.main()
