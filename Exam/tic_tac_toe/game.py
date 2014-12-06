import random


class Game:

    def __init__(self):
        self._map = ['.', '.', '.', '.', '.', '.', '.', '.', '.']

    def __str__(self):
        result = ""
        for elem in range(1, 10):
            result += self._map[elem - 1]
            if elem % 3 != 0:
                result += "    "
            else:
                result += "\n"
        return result

    def check_left_diagonal(self, player_symbol):
        return self._map[0] == player_symbol and self._map[4] == player_symbol and self._map[8] == player_symbol

    def check_right_diagonal(self, player_symbol):
        return self._map[2] == player_symbol and self._map[4] == player_symbol and self._map[6] == player_symbol

    def check_columns(self, player_symbol):
        for x in range(0, 3):
            if self._map[x] == player_symbol and self._map[x + 3] == player_symbol and self._map[x + 6] == player_symbol:
                return True
        return False

    def check_rows(self, player_symbol):
        for x in range(0, 3):
            if self._map[x * 3] == player_symbol and self._map[(x * 3) + 1] == player_symbol and self._map[(x * 3) + 2] == player_symbol:
                return True
        return False

    def is_anyone_win(self, player_symbol):
        return self.check_columns(player_symbol) or self.check_rows(player_symbol) or self.check_left_diagonal(player_symbol) or\
            self.check_left_diagonal(player_symbol) or self.check_right_diagonal(player_symbol)

    def is_cell_free(self, cell_position):
        return self._map[cell_position] == "."

    def is_have_not_free_cells(self):
        for elem in self._map:
            if elem == ".":
                return False
        return True

    def set_X_from_player_turn(self, inputed_num):
        if self._map[inputed_num - 1] == ".":
            self._map[inputed_num - 1] = "X"
            return True
        else:
            return False

    def set_O_from_computer_easy(self):
        flag = False
        while not flag:
            position = random.randint(0, 8)

            if self.is_cell_free(position):
                flag = True
                self._map[position] = "O"
            elif self.is_have_not_free_cells():
                return False
        return True

    def check_can_win(self, player_symbol, fst_num, snd_num, trd_num):
        return (self._map[fst_num] == player_symbol and self._map[snd_num] == player_symbol) and self._map[trd_num] == "." or\
            (self._map[fst_num] == player_symbol and self._map[trd_num] == player_symbol) and self._map[snd_num] == "." or\
            (self._map[snd_num] == player_symbol and self._map[trd_num] == player_symbol) and self._map[fst_num] == "."

    def can_win_left_diagonal(self, player_symbol):
        return self.check_can_win(player_symbol, 0, 4, 8)

    def can_win_right_diagonal(self, player_symbol):
        return self.check_can_win(player_symbol, 2, 4, 6)

    def can_win_any_column(self, player_symbol, num_of_column):
        return self.check_can_win(player_symbol, num_of_column, num_of_column + 3, num_of_column + 6)

    def can_win_any_row(self, player_symbol, num_of_row):
        return self.check_can_win(player_symbol, num_of_row * 3, (num_of_row * 3) + 1, (num_of_row * 3) + 2)

    def set_simbol_to_free_cell(self, player_symbol, fst_num, snd_num, trd_num):
        if self._map[fst_num] == ".":
            self._map[fst_num] = player_symbol
        elif self._map[snd_num] == ".":
            self._map[snd_num] = player_symbol
        else:
            self._map[trd_num] = player_symbol

    def win_if_possible(self, player_symbol):
        if self.can_win_left_diagonal(player_symbol):
            self.set_simbol_to_free_cell(player_symbol, 0, 4, 8)
            return True

        if self.can_win_right_diagonal(player_symbol):
            self.set_simbol_to_free_cell(player_symbol, 2, 4, 6)
            return True

        for x in range(0, 3):
            if self.can_win_any_column(player_symbol, x):
                self.set_simbol_to_free_cell(player_symbol, x, x + 3, x + 6)
                return True

            if self.can_win_any_row(player_symbol, x):
                self.set_simbol_to_free_cell(player_symbol, x * 3, (x * 3) + 1, (x * 3) + 2)
                return True

        return False

    def stop_player_from_winning_if_possible(self, enemy_player_symbol):
        player_symbol = "O"
        if enemy_player_symbol == "O":
            player_symbol = "X"

        if self.can_win_left_diagonal(enemy_player_symbol):
            self.set_simbol_to_free_cell(player_symbol, 0, 4, 8)
            return True

        if self.can_win_right_diagonal(enemy_player_symbol):
            self.set_simbol_to_free_cell(player_symbol, 2, 4, 6)
            return True

        for x in range(0, 3):
            if self.can_win_any_column(enemy_player_symbol, x):
                self.set_simbol_to_free_cell(player_symbol, x, x + 3, x + 6)
                return True

            if self.can_win_any_row(enemy_player_symbol, x):
                self.set_simbol_to_free_cell(player_symbol, x * 3, (x * 3) + 1, (x * 3) + 2)
                return True

        return False

    def check_all_is_free_withoute_one(self, num_of_not_free_cell):
        is_all_free = True
        for x in range(0, 9):
            if x == num_of_not_free_cell:
                pass
            elif self._map[x] != ".":
                is_all_free = False
        return is_all_free

    def enemy_start_in_corner(self, enemy_player_symbol):
        if self._map[0] == enemy_player_symbol:
            return self.check_all_is_free_withoute_one(0)
        if self._map[2] == enemy_player_symbol:
            return self.check_all_is_free_withoute_one(2)
        if self._map[6] == enemy_player_symbol:
            return self.check_all_is_free_withoute_one(6)
        if self._map[8] == enemy_player_symbol:
            return self.check_all_is_free_withoute_one(8)
        return False

    def enemy_start_in_center(self, enemy_player_symbol):
        if self._map[4] == enemy_player_symbol:
            return self.check_all_is_free_withoute_one(4)
        return False

    def get_opposite_symbol(self, enemy_player_symbol):
        player_symbol = "O"
        if enemy_player_symbol == "O":
            player_symbol = "X"
        return player_symbol

    def strategy_tripple_with_opposite(self, enemy_player_symbol):
        player_symbol = self.get_opposite_symbol(enemy_player_symbol)

        if (self._map[0] == enemy_player_symbol and self._map[8] == enemy_player_symbol) or\
           (self._map[2] == enemy_player_symbol and self._map[6] == enemy_player_symbol):
            position = random.choice([1, 3, 5, 7])
            if self.is_cell_free(position):
                self._map[position] = player_symbol
                return True

        return False

    def strategy_tripple_with_corner(self, enemy_player_symbol):
        player_symbol = self.get_opposite_symbol(enemy_player_symbol)

        if self._map[2] == enemy_player_symbol and self._map[3] == enemy_player_symbol:
            if self.is_cell_free(0):
                self._map[0] = player_symbol
                return True

        if self._map[5] == enemy_player_symbol and self._map[6] == enemy_player_symbol:
            if self.is_cell_free(6):
                self._map[6] = player_symbol
                return True

        if self._map[0] == enemy_player_symbol and self._map[5] == enemy_player_symbol:
            if self.is_cell_free(8):
                self._map[8] = player_symbol
                return True

        if self._map[3] == enemy_player_symbol and self._map[8] == enemy_player_symbol:
            if self.is_cell_free(2):
                self._map[2] = player_symbol
                return True

        return False

    def strategy_in_first_move_in_corner(self, enemy_player_symbol):
        player_symbol = self.get_opposite_symbol(enemy_player_symbol)

        if self.enemy_start_in_corner(enemy_player_symbol):
            self._map[4] = player_symbol
            return True

        return False

    def strategy_in_first_move_in_center(self, enemy_player_symbol):
        player_symbol = self.get_opposite_symbol(enemy_player_symbol)

        if self.enemy_start_in_center(enemy_player_symbol):
            position = random.choice([0, 2, 6, 8])
            self._map[position] = player_symbol
            return True

        return False

    def strategy_tripple_with_first_move_in_centre(self, enemy_player_symbol):
        player_symbol = self.get_opposite_symbol(enemy_player_symbol)

        if (self._map[0] == enemy_player_symbol and self._map[4] == enemy_player_symbol and self._map[8] == player_symbol) or\
           (self._map[4] == enemy_player_symbol and self._map[8] == enemy_player_symbol and self._map[0] == player_symbol) or\
           (self._map[2] == enemy_player_symbol and self._map[4] == enemy_player_symbol and self._map[6] == player_symbol) or\
           (self._map[4] == enemy_player_symbol and self._map[6] == enemy_player_symbol and self._map[2] == player_symbol):
            position = random.choice([0, 2, 6, 8])
            if self.is_cell_free(position):
                self._map[position] = player_symbol
                return True

        return False

    def counterPlayerStrategyIfPossible(self, enemy_player_symbol):
        if self.strategy_in_first_move_in_center(enemy_player_symbol):
            return True

        if self.strategy_in_first_move_in_corner(enemy_player_symbol):
            return True

        if self.strategy_tripple_with_opposite(enemy_player_symbol):
            return True

        if self.strategy_tripple_with_corner(enemy_player_symbol):
            return True

        return False

    def set_O_from_computer_imposible(self):
        if self.win_if_possible("O"):
            return True

        if self.stop_player_from_winning_if_possible("X"):
            return True

        if self.counterPlayerStrategyIfPossible("X"):
            return True

        return self.set_O_from_computer_easy()


def main():
    my_game = Game()
    print(my_game)
    while (not my_game.is_anyone_win("X") and not my_game.is_anyone_win("O")) and not my_game.is_have_not_free_cells():
        turn = input("Its your turn :) Enter the num from 1 to 9:\n?> ")
        if my_game.set_X_from_player_turn(int(turn)) and not my_game.is_anyone_win("X"):
                if not my_game.set_O_from_computer_imposible():
                    print(my_game)
                    break
        print(my_game)
    if my_game.is_anyone_win("X"):
        print("You win. :) Congratulations")
    elif my_game.is_anyone_win("O"):
        print("You lose. :(")
    else:
        print("Drawn")


if __name__ == '__main__':
    main()
