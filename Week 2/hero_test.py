import unittest

from hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.bron_hero.known_as(), "Bron the DragonSlayer")

    def test_get_health(self):
        self.assertEqual(self.bron_hero.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.bron_hero.is_alive())

    def test_is_not_alive(self):
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.is_alive())

    def test_take_damage(self):
        self.bron_hero.take_damage(30)
        self.assertEqual(self.bron_hero.health, 70)

    def test_take_damage_more_than_hp(self):
        self.bron_hero.take_damage(120)
        self.assertEqual(self.bron_hero.health, 0)

    def test_take_healing(self):
        self.bron_hero.health = 70
        temp_heal = self.bron_hero.take_healing(20)
        self.assertTrue(self.bron_hero.take_healing(20))
        self.assertTrue(temp_heal)

    def test_take_healing_on_dead_hero(self):
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.take_healing(50))

    def test_take_healing_over_max_hp(self):
        self.bron_hero.health = 70
        temp_heal = self.bron_hero.take_healing(50)
        self.assertTrue(self.bron_hero.take_healing(50))
        self.assertTrue(temp_heal)

if __name__ == '__main__':
    unittest.main()
