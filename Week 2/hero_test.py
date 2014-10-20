import unittest

from hero import Hero


class TestHero(unittest.TestCase):

    def test_hero_init(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")

    def test_known_as(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")
        self.assertEqual(self.bron_hero.known_as(), "Bron the DragonSlayer")

if __name__ == '__main__':
    unittest.main()
