import unittest

from next_hack import next_hack, is_list_palindrome, number_to_binary, hack_number


class Next_hack_test(unittest.TestCase):

    def test_is_list_palindrome_third(self):
        self.assertTrue(is_list_palindrome([1, 1, 1, 1]))
        self.assertFalse(is_list_palindrome([4, 2, 1]))
        self.assertTrue(is_list_palindrome([4, 2, 2, 4]))
        self.assertTrue(is_list_palindrome([1]))
        self.assertTrue(is_list_palindrome([1, 2, 3, 3, 2, 1]))
        self.assertFalse(is_list_palindrome([0, 1, 1]))

    def test_number_to_binary(self):
        self.assertEqual(number_to_binary(1), [1])
        self.assertEqual(number_to_binary(7919), [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1])
        self.assertEqual(number_to_binary(7), [1, 1, 1])
        self.assertEqual(number_to_binary(6), [0, 1, 1])

    def test_hack_number(self):
        self.assertTrue(hack_number(1))
        self.assertTrue(hack_number(7919))
        self.assertTrue(hack_number(7))
        self.assertFalse(hack_number(6))

    def test_next_hack(self):
        self.assertEqual(next_hack(0), 1)
        self.assertEqual(next_hack(10), 21)
        self.assertEqual(next_hack(8031), 8191)

if __name__ == '__main__':
    unittest.main()
