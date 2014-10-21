import unittest

from count_consonants import count_consonants


class Count_consonants_test(unittest.TestCase):

    def test_count_consonants(self):
        self.assertEqual(count_consonants("Python"), 4)
        self.assertEqual(count_consonants("Theistareykjarbunga"), 11)
        self.assertEqual(count_consonants("grrrrgh!"), 7)
        self.assertEqual(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"), 44)
        self.assertEqual(count_consonants("A nice day to code!"), 6)

if __name__ == '__main__':
    unittest.main()
