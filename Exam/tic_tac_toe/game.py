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

    def set_X_from_player_turn(self, inputed_num):
        if self._map[inputed_num - 1] == ".":
            self._map[inputed_num - 1] = "X"

    def set_O_from_computer(self):


def main():
    my_game = Game()
    while True:
        print(my_game)
        turn = input("Its your turn :) Enter the num from 1 to 9:\n?> ")
        my_game.set_X_from_player_turn(int(turn))


if __name__ == '__main__':
    main()
