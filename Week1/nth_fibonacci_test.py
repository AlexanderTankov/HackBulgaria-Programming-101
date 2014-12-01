import unittest

from nth_fibonacci import nth_fibonacci, nth_fibonacci_second


class Nth_fibonacci_test(unittest.TestCase):

    def test_nth_fibonacci(self):
        self.assertEqual(nth_fibonacci(1), 1)
        self.assertEqual(nth_fibonacci(2), 1)
        self.assertEqual(nth_fibonacci(3), 2)
        self.assertEqual(nth_fibonacci(10), 55)

    def test_nth_fibonacci_second(self):
        self.assertEqual(nth_fibonacci_second(1), 1)
        self.assertEqual(nth_fibonacci_second(2), 1)
        self.assertEqual(nth_fibonacci_second(3), 2)
        self.assertEqual(nth_fibonacci_second(10), 55)

if __name__ == '__main__':
    unittest.main()
