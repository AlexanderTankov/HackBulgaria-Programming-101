from orc import Orc


class Dungeon():

    def __init__(self, file_path):
        self.file_path = file_path

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

        for char in temp:
            if char == "S":
                temp = temp.replace("S", "%s" % char_for_change, 1)
                filename = "%s" % self.file_path
                my_file = open(filename, 'w')
                new_content = temp
                my_file.write("".join(new_content))
                my_file.close()
                return True
        return False

    def move(self, player_name, direction):
        temp = self.print_map()
