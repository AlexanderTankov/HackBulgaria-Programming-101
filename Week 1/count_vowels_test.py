import unittest

from count_vowels import count_vowels


class Count_vowels_test(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Python"), 2)
        self.assertEqual(count_vowels("Theistareykjarbunga"), 8)
        self.assertEqual(count_vowels("grrrrgh!"), 0)
        self.assertEqual(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"), 22)
        self.assertEqual(count_vowels("A nice day to code!"), 8)

if __name__ == '__main__':
    unittest.main()
