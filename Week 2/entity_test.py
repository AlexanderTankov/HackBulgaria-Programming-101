import unittest

from entity import Entity
from weapon import Weapon


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.bron_entity = Entity("Bron", 100)

    def test_entity_init(self):
        self.assertEqual(self.bron_entity.name, "Bron")
        self.assertEqual(self.bron_entity.health, 100)

    def test_get_health(self):
        self.assertEqual(self.bron_entity.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.bron_entity.is_alive())

    def test_is_not_alive(self):
        self.bron_entity.health = 0
        self.assertFalse(self.bron_entity.is_alive())

    def test_take_damage(self):
        self.bron_entity.take_damage(30)
        self.assertEqual(self.bron_entity.health, 70)

    def test_take_damage_more_than_hp(self):
        self.bron_entity.take_damage(120)
        self.assertEqual(self.bron_entity.health, 0)

    def test_take_healing(self):
        self.bron_entity.health = 70
        temp_heal = self.bron_entity.take_healing(20)
        self.assertTrue(self.bron_entity.take_healing(20))
        self.assertTrue(temp_heal)

    def test_take_healing_on_dead_hero(self):
        self.bron_entity.health = 0
        self.assertFalse(self.bron_entity.take_healing(50))

    def test_take_healing_over_max_hp(self):
        self.bron_entity.health = 70
        temp_heal = self.bron_entity.take_healing(50)
        self.assertTrue(self.bron_entity.take_healing(50))
        self.assertTrue(temp_heal)

    def test_has_weapon_when_dont_have(self):
        self.assertFalse(self.bron_entity.has_weapon())

    def test_has_weapon_when_have(self):
        axe = Weapon("Mighty Axe", 25, 0.2)
        self.bron_entity.equip_weapon(axe)
        self.assertTrue(self.bron_entity.has_weapon())

    def test_equip_weapon(self):
        axe = Weapon("Mighty Axe", 25, 0.2)
        self.bron_entity.equip_weapon(axe)
        self.assertEqual(self.bron_entity.weapon, axe)

    def test_attack_when_entity_dont_have_weapon(self):
        self.assertEqual(self.bron_entity.damage, 0)

    def test_attack_when_entity_have_weapon(self):
        axe = Weapon("Mighty Axe", 25, 0.2)
        self.bron_entity.equip_weapon(axe)
        self.assertEqual(self.bron_entity.damage, self.bron_entity.attack())

if __name__ == '__main__':
    unittest.main()
