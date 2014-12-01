import unittest

from zero_insert import zero_insert


class Zero_insert_test(unittest.TestCase):

    def test_zero_insert(self):
        self.assertEqual(zero_insert(116457), 10160457)
        self.assertEqual(zero_insert(55555555), 505050505050505)
        self.assertEqual(zero_insert(1), 1)
        self.assertEqual(zero_insert(6446), 6040406)

if __name__ == '__main__':
    unittest.main()
