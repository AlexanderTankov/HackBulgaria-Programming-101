import unittest

from list_to_number import list_to_number


class List_to_number_test(unittest.TestCase):

    def test_list_to_number(self):
        self.assertEqual(list_to_number([1, 2, 3]), 123)
        self.assertEqual(list_to_number([9, 9, 9, 9, 9]), 99999)
        self.assertEqual(list_to_number([1, 2, 3, 0, 2, 3]), 123023)

if __name__ == '__main__':
    unittest.main()
