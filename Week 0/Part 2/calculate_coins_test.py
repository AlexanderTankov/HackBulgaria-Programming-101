import unittest

from calculate_coins import calculate_coins


class Calculate_coins_test(unittest.TestCase):

    def test_calculate_coins(self):
        self.assertEqual(calculate_coins(0.53), {'1': 1, '2': 1, '100': 0, '5': 0, '10': 0, '50': 1, '20': 0})
        self.assertEqual(calculate_coins(8.94), {'1': 0, '2': 2, '100': 8, '5': 0, '10': 0, '50': 1, '20': 2})

if __name__ == '__main__':
    unittest.main()
