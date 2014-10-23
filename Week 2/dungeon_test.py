import unittest

from hero import Hero
from orc import Orc
from dungeon import Dungeon


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.my_map = Dungeon("basic_dungeon.txt")
        my_file = open("basic_dungeon.txt", 'w')
        new_content = "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S\n"
        my_file.write("".join(new_content))
        my_file.close()

    def test_dungeon_init(self):
        self.assertEqual(self.my_map.file_path, "basic_dungeon.txt")

    def test_print_map(self):
        self.assertEqual(self.my_map.print_map(), "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S\n")

    def test_spawn(self):
        bron_orc = Orc("Bron", 100, 1.3)
        self.assertTrue(self.my_map.spawn("player_1", bron_orc))

    def test_spawn_when_dont_have_spowning_point(self):
        bron_orc = Orc("Bron", 100, 1.3)
        bron_hero = Hero("Bron", 100, "DragonSlayer")
        self.my_map.spawn("player_1", bron_orc)
        self.my_map.spawn("player_2", bron_hero)
        self.assertFalse(self.my_map.spawn("player_3", bron_orc))

    def test_move_on_map(self):
        bron_orc = Orc("Bron", 100, 1.3)
        bron_hero = Hero("Bron", 100, "DragonSlayer")
        self.my_map.spawn("player_1", bron_orc)
        self.my_map.spawn("player_2", bron_hero)
        self.assertFalse(self.my_map.move("player_1", "left"))
        self.assertTrue(self.my_map.move("player_1", "right"))
        self.assertFalse(self.my_map.move("player_1", "up"))
        self.assertFalse(self.my_map.move("player_1", "right"))
        self.assertFalse(self.my_map.move("player_2", "down"))
        self.assertTrue(self.my_map.move("player_2", "up"))

if __name__ == '__main__':
    unittest.main()
