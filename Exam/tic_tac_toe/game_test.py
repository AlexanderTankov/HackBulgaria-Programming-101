import unittest

from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.test_game = Game()

    def test_check_left_diagonal_is_true(self):
        self.test_game._map = ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']
        self.assertTrue(self.test_game.check_left_diagonal("X"))

    def test_check_left_diagonal_is_false_with_worng_symbol(self):
        self.test_game._map = ['X', '.', '.', '.', 'X', '.', '.', '.', 'X']
        self.assertFalse(self.test_game.check_left_diagonal("Y"))

    def test_check_right_diagonal_is_true(self):
        self.test_game._map = ['.', '.', 'X', '.', 'X', '.', 'X', '.', '.']
        self.assertTrue(self.test_game.check_right_diagonal("X"))

    def test_check_right_diagonal_is_false_with_worng_symbol(self):
        self.test_game._map = ['.', '.', 'X', '.', 'X', '.', 'X', '.', '.']
        self.assertFalse(self.test_game.check_right_diagonal("Y"))

    def test_check_columns_is_true(self):
        self.test_game._map = ['X', '.', '.', 'X', '.', '.', 'X', '.', '.']
        self.assertTrue(self.test_game.check_columns("X"))

    def test_check_columns_is_false_with_worng_symbol(self):
        self.test_game._map = ['X', '.', 'X', 'X', 'X', '.', 'X', '.', '.']
        self.assertFalse(self.test_game.check_columns("Y"))

    def test_check_rows_is_true(self):
        self.test_game._map = ['X', 'X', 'X', '.', 'X', '.', 'X', '.', '.']
        self.assertTrue(self.test_game.check_rows("X"))

    def test_check_rows_is_false_with_worng_symbol(self):
        self.test_game._map = ['X', 'X', 'X', 'X', 'X', '.', 'X', '.', '.']
        self.assertFalse(self.test_game.check_rows("Y"))

    def test_is_anyone_win_is_true(self):
        self.test_game._map = ['X', 'X', 'X', '.', 'X', '.', 'X', '.', '.']
        self.assertTrue(self.test_game.is_anyone_win("X"))

    def test_is_anyone_win_is_false_with_worng_symbol(self):
        self.test_game._map = ['X', 'X', 'X', '.', 'X', '.', 'X', '.', '.']
        self.assertFalse(self.test_game.is_anyone_win("Y"))

    def test_is_cell_free_is_true(self):
        self.test_game._map = ['X', '.', 'X', '.', 'X', '.', '.', 'X', '.']
        self.assertTrue(self.test_game.is_cell_free(1))

    def test_is_have_not_free_cells_is_true(self):
        self.test_game._map = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O']
        self.assertTrue(self.test_game.is_have_not_free_cells())

    def test_set_X_from_player_turn_is_true(self):
        self.test_game.set_X_from_player_turn(1)
        self.assertEqual(self.test_game._map[0], "X")

if __name__ == '__main__':
    unittest.main()
