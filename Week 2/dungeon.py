from orc import Orc
from fight import Fight


class Dungeon():

    def __init__(self, file_path):
        self.file_path = file_path
        self.heroes_list = []
        self.heroes_dict = {}

    def print_map(self):
        filename = "%s" % self.file_path
        my_file = open(filename, 'r')
        content = my_file.read()
        my_file.close()
        return content

    def spawn(self, player_name, entity):
        temp = self.print_map()
        char_for_change = ""
        if isinstance(entity, Orc):
            char_for_change = "O"
        else:
            char_for_change = "H"
        #check that player is in dict
        player_is_in_dict = False
        for keys in self.heroes_dict:
            if keys == "%s" % (player_name):
                player_is_in_dict = True

        for char in range(0, len(temp)):
            if temp[char] == "S":
                temp = temp.replace("S", "%s" % char_for_change, 1)
                #add hero cordinats to hero list
                if not player_is_in_dict:
                    #add player in dict
                    self.heroes_dict[entity] = "%s" % (player_name)
                    #add player in list
                    self.heroes_list.append(["%s" % (player_name), char])
                #save new map to file
                filename = "%s" % self.file_path
                my_file = open(filename, 'w')
                new_content = temp
                my_file.write("".join(new_content))
                my_file.close()
                return True
        return False

    def get_entity_pos(self, player_name):
        for heroes in self.heroes_list:
            if heroes[0] == "%s" % (player_name):
                return heroes[1]

    def get_entity_name(self, player_pos):
        for heroes in self.heroes_list:
            if heroes[1] == player_pos:
                return heroes[0]

    def compleate_fight(self, player_name, player_pos):
        enemy_name = self.get_entity_name(player_pos)
        #get player from dict
        for keys in self.heroes_dict:
            if keys == "%s" % (enemy_name) or keys == "%s" % (player_name):
                if keys == "%s" % (player_name):
                    player_one = self.heroes_dict[keys]
                if keys == "%s" % (enemy_name):
                    player_two = self.heroes_dict[keys]
        fight = Fight(player_one, player_two)
        fight.simulate_fight()

    def move(self, player_name, direction):
        temp = self.print_map()
        #get position of hero
        player_posicion = self.get_entity_pos(player_name)

        if direction == "right":
            if (player_posicion - 1) < len(temp):
                if temp[player_posicion + 1] == "\n" or temp[player_posicion + 1] == "#":
                    return False
                elif temp[player_posicion + 1] == ".":
                    player_posicion += 1
                    for heroes in self.heroes_list:
                        if heroes[0] == "%s" % (player_name):
                            heroes[1] = player_posicion
                    return True
                elif temp[player_posicion + 1] == "H" or temp[player_posicion + 1] == "O":
                    self.compleate_fight(player_name, player_posicion + 1)
            else:
                return False

        if direction == "left":
            if (player_posicion - 1) > 0:
                if temp[player_posicion - 1] == "\n" or temp[player_posicion - 1] == "#":
                    return False
                elif temp[player_posicion - 1] == ".":
                    player_posicion -= 1
                    for heroes in self.heroes_list:
                        if heroes[0] == "%s" % (player_name):
                            heroes[1] = player_posicion
                    return True
                elif temp[player_posicion - 1] == "H" or temp[player_posicion - 1] == "O":
                    self.compleate_fight(player_name, player_posicion - 1)
            else:
                return False

        num_of_columns = 0
        for char in temp:
            if char != "\n":
                num_of_columns += 1
            else:
                break

        if direction == "up":
            if (player_posicion - (num_of_columns + 1)) > 0:
                if temp[player_posicion - (num_of_columns + 1)] == "\n" or temp[player_posicion - (num_of_columns + 1)] == "#":
                    return False
                elif temp[player_posicion - (num_of_columns + 1)] == ".":
                    player_posicion -= (num_of_columns + 1)
                    for heroes in self.heroes_list:
                        if heroes[0] == "%s" % (player_name):
                            heroes[1] = player_posicion
                    return True
                elif temp[player_posicion - (num_of_columns + 1)] == "H" or temp[player_posicion - (num_of_columns + 1)] == "O":
                    self.compleate_fight(player_name, player_posicion - (num_of_columns + 1))
            else:
                return False

        if direction == "down":
            if (player_posicion + (num_of_columns + 1)) < len(temp):
                if temp[player_posicion + (num_of_columns + 1)] == "\n" or temp[player_posicion + (num_of_columns + 1)] == "#":
                    return False
                elif temp[player_posicion + (num_of_columns + 1)] == ".":
                    player_posicion += (num_of_columns + 1)
                    for heroes in self.heroes_list:
                        if heroes[0] == "%s" % (player_name):
                            heroes[1] = player_posicion
                    return True
                elif temp[player_posicion - (num_of_columns + 1)] == "H" or temp[player_posicion - (num_of_columns + 1)] == "O":
                    self.compleate_fight(player_name, player_posicion + (num_of_columns + 1))
            else:
                return False
