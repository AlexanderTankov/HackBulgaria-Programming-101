import unittest

from orc import Orc


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.bron_orc = Orc("Bron", 100, 1.3)

    def test_orc_init(self):
        self.assertEqual(self.bron_orc.berserk_factor, 1.3)

    def test_init_incorect_berserk_factor(self):
        with self.assertRaises(ValueError):
            Orc("Bron", 100, 2.3)

    def test_attack(self):
        self.assertEqual(self.bron_orc.attack(), self.bron_orc.damage)
        
if __name__ == '__main__':
    unittest.main()
