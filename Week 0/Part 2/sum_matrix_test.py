import unittest

from sum_matrix import sum_matrix


class Sum_matrix_test(unittest.TestCase):

    def test_sum_matrix(self):
        self.assertEqual(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)
        self.assertEqual(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)
        self.assertEqual(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), 55)

if __name__ == '__main__':
    unittest.main()
