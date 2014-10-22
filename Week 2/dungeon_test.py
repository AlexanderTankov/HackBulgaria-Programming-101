import unittest

from dungeon import Dungeon


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.my_map = Dungeon("basic_dungeon.txt")

    def test_dungeon_init(self):
        self.assertEqual(self.my_map.file_path, "basic_dungeon.txt")

    def test_print_map(self):
        self.assertEqual(self.my_map.print_map(), "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S\n")

if __name__ == '__main__':
    unittest.main()
