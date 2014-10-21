import unittest

from is_int_palindrome import is_int_palindrome, is_int_palindrome_snd


class Is_int_palindrome_test(unittest.TestCase):

    def test_is_int_palindrome(self):
        self.assertTrue(is_int_palindrome(1))
        self.assertFalse(is_int_palindrome(42))
        self.assertTrue(is_int_palindrome(100001))
        self.assertTrue(is_int_palindrome(9))
        self.assertFalse(is_int_palindrome(123))

    def test_is_int_palindrome_snd(self):
        self.assertTrue(is_int_palindrome_snd(1))
        self.assertFalse(is_int_palindrome_snd(42))
        self.assertTrue(is_int_palindrome_snd(100001))
        self.assertTrue(is_int_palindrome_snd(9))
        self.assertFalse(is_int_palindrome_snd(123))

if __name__ == '__main__':
    unittest.main()
