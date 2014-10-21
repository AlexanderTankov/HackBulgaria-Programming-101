import unittest

from number_to_list import number_to_list


class Number_to_list_test(unittest.TestCase):

    def test_number_to_list(self):
        self.assertEqual(number_to_list(123), [1, 2, 3])
        self.assertEqual(number_to_list(99999), [9, 9, 9, 9, 9])
        self.assertEqual(number_to_list(123023), [1, 2, 3, 0, 2, 3])

if __name__ == '__main__':
    unittest.main()
