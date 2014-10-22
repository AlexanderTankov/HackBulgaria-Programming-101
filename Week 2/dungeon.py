class Dungeon():

    def __init__(self, file_path):
        self.file_path = file_path

    def print_map(self):
        filename = "%s" % self.file_path
        my_file = open(filename, 'r')
        content = my_file.read()
        my_file.close()
        print(content)
        return content
