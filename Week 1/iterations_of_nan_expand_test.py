import unittest

from iterations_of_nan_expand import iterations_of_nan_expand


class Iterations_of_nan_expand_test(unittest.TestCase):

    def test_iterations_of_nan_expand(self):
        self.assertEqual(iterations_of_nan_expand(""), 0)
        self.assertEqual(iterations_of_nan_expand("Not a NaN"), 1)
        self.assertEqual(iterations_of_nan_expand("Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN"), 10)

    def test_iteration_of_nan_expand_with_incorect_string(self):
        self.assertFalse(iterations_of_nan_expand("Show these people!"))


if __name__ == '__main__':
    unittest.main()
