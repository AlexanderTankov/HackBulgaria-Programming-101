import unittest

from weapon import Weapon


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.axe = Weapon("Mighty Axe", 25, 0.2)

    def test_entity_init(self):
        self.assertEqual(self.axe.type, "Mighty Axe")
        self.assertEqual(self.axe.damage, 25)
        self.assertEqual(self.axe.critical_strike_percent, 0.2)

    def test_critical_hit(self):
        self.assertTrue(self.axe.critical_hit())

if __name__ == '__main__':
    unittest.main()
