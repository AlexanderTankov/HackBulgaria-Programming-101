import unittest

from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class TestFight(unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")
        self.axe = Weapon("Mighty Axe", 25, 0.2)
        self.sword = Weapon("Mighty Sword", 12, 0.7)
        self.bron_orc = Orc("Bron", 100, 1.3)
        self.my_fight = Fight(self.bron_hero, self.bron_orc)
        self.bron_hero.weapon = self.sword
        self.bron_orc.weapon = self.axe

    def test_fight_init(self):
        self.assertEqual(self.my_fight.hero, self.bron_hero)
        self.assertEqual(self.my_fight.orc, self.bron_orc)

    def test_who_is_first(self):
        flag_hero = False
        flag_orc = False
        for i in range(0, 10):
            self.my_fight.who_is_first()
            if self.my_fight.who_is_first() == self.bron_hero:
                flag_hero = True
            else:
                flag_orc = True
        self.assertTrue(flag_hero and flag_orc)

    def test_simulate_fight(self):
        self.my_fight.simulate_fight()
        self.assertFalse(self.bron_orc.is_alive() and self.bron_hero.is_alive())

    def test_simulate_fight_hero_wtih_wep_vs_hero_without_wep(self):
        self.hero_without_wep = Hero("Toni", 100, "Monster")
        self.fight = Fight(self.bron_hero, self.hero_without_wep)
        self.fight.simulate_fight()
        self.assertFalse(self.hero_without_wep.is_alive())

    def test_simulate_fight_hero_vs_equal_orc(self):
        self.equal_orc = Orc("Toni", 100, 1.5)
        self.equal_orc.weapon = self.sword
        self.fight = Fight(self.bron_hero, self.equal_orc)
        self.fight.simulate_fight()
        self.assertFalse(self.bron_hero.is_alive())

if __name__ == '__main__':
    unittest.main()
