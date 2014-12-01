import random
from CreateDB import High_Score
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from CreateDB import Base


MIN_NUMBER = 1
MAX_NUMBER = 10
NUM_OF_CHARACTERS = 4


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 1


class Game:

    def __init__(self):
        self.player = ""
        self._characters = ['+', '-', '^', 'x']
        self.high_score = []

    def generate_num(self):
        return random.randint(MIN_NUMBER, MAX_NUMBER)

    def generate_character(self):
        return random.randint(0, NUM_OF_CHARACTERS - 1)

    def sum_expression(self, left_num, right_num, character_num):
        if self._characters[character_num] == '+':
            return left_num + right_num
        elif self._characters[character_num] == '-':
            return left_num - right_num
        elif self._characters[character_num] == '^':
            result = 1
            if right_num == 0:
                return 1
            while right_num != 0:
                result *= left_num
                right_num -= 1
            return result
        else:
            return left_num * right_num

    def save_player_in_DB(self):
        engine = create_engine("sqlite:///High_Score.db")
        Base.metadata.create_all(engine)

        my_session = Session(bind=engine)
        new_player = High_Score(
            player_name=self.player.name,
            score=self.player.score*self.player.score
        )

        my_session.add(new_player)
        my_session.commit()

    def view_high_scores(self):
        engine = create_engine("sqlite:///High_Score.db")
        Base.metadata.create_all(engine)

        session = Session(bind=engine)
        results = session.query(High_Score).all()

        print("This is the current top10:")
        for result in results:
            print("{}. {} with {} points".format(result.id, result.player_name, result.score))

    def start(self):
        player_name = input("Enter your playername>")
        self.player = Player(player_name)
        print("Welcome {}! Let the game begin!".format(self.player.name))

        is_correct = True
        while is_correct:
            left_num = self.generate_num()
            right_num = self.generate_num()
            character_num = self.generate_character()

            print("Question #{}:\n\
What is the answer to {} {} {}?".format(self.player.score, left_num, self._characters[character_num], right_num))

            answer = input("?>")
            if int(answer) != self.sum_expression(left_num, right_num, character_num):
                is_correct = False
                print("Incorrect! Ending game. You score is: {}".format(self.player.score * self.player.score))
                self.save_player_in_DB()
            else:
                self.player.score += 1
                print("Correct!")


def main():
    flag = False
    while not flag:
        answer = input("Welcome to the \"Do you even math?\" game!\n\
Here are your options:\n\
- start\n\
- high scores\n\
?>")
        my_game = Game()
        if answer.lower() == "start":
            flag = True
            my_game.start()
        elif answer.lower() == "high scores":
            flag = True
            my_game.view_high_scores()
        else:
            print("Wrong answer!")

if __name__ == '__main__':
    main()
