import unittest

from orc import Orc


class TestOrc(unittest.TestCase):

    def test_orc_init(self):
        self.bron_orc = Orc("Bron", 100, 1)
        self.assertEqual(self.bron_orc.berserk_factor, 1)

if __name__ == '__main__':
    unittest.main()
