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

    def check_left_diagonal(self, player_simbol):
        return self._map[0] == player_simbol and self._map[4] == player_simbol and self._map[8] == player_simbol

    def check_right_diagonal(self, player_simbol):
        return self._map[2] == player_simbol and self._map[4] == player_simbol and self._map[6] == player_simbol

    def check_columns(self, player_simbol):
        for x in range(0, 3):
            if self._map[x] == player_simbol and self._map[x + 3] == player_simbol and self._map[x + 6] == player_simbol:
                return True
        return False

    def check_rows(self, player_simbol):
        for x in range(0, 3):
            if self._map[x * 3] == player_simbol and self._map[(x * 3) + 1] == player_simbol and self._map[(x * 3) + 2] == player_simbol:
                return True
        return False

    def is_anyone_win(self, player_simbol):
        return self.check_columns(player_simbol) or self.check_rows(player_simbol) or self.check_left_diagonal(player_simbol) or\
            self.check_left_diagonal(player_simbol) or self.check_right_diagonal(player_simbol)

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

    # def set_O_from_computer_imposible(self):
    #     if win_if_possible():
    #         pass

    #     if stop_player_from_winning_if_possible():
    #         pass

    #     if counterPlayerStrategyIfPossible():
    #         pass


def main():
    my_game = Game()
    print(my_game)
    while (not my_game.is_anyone_win("X") and not my_game.is_anyone_win("O")) or my_game.is_have_not_free_cells():
        turn = input("Its your turn :) Enter the num from 1 to 9:\n?> ")
        if my_game.set_X_from_player_turn(int(turn)) and not my_game.is_anyone_win("X"):
                if not my_game.set_O_from_computer_easy():
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
