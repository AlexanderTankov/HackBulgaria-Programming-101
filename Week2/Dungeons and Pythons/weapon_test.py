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
        flag_true = False
        flag_false = False
        for i in range(0, 1000):
            if self.axe.is_critical_hit():
                flag_true = True
            else:
                flag_false = True
        self.assertTrue(flag_false and flag_true)

if __name__ == '__main__':
    unittest.main()
