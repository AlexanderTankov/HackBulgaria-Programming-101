import unittest

from CashDeck import CashDeck


class CashDeskTest(unittest.TestCase):

    def setUp(self):
        self.new_cash_desk = CashDeck()

    def test_total_zero_when_new_instance_made(self):
        self.assertEqual(self.new_cash_desk.total(), 0)

    def test_total_after_money_take(self):
        self.new_cash_desk.take_money({1: 2, 100: 3})
        self.assertEqual(self.new_cash_desk.total(), 302)

    def test_can_withdraw_all_money(self):
        self.new_cash_desk.take_money({1: 2, 100: 3})
        self.assertTrue(self.new_cash_desk.can_withdraw_money(302))

    def test_can_withdraw_not_all_money(self):
        self.new_cash_desk.take_money({1: 2, 100: 3})
        self.assertTrue(self.new_cash_desk.can_withdraw_money(301))

    def test_cant_withdraw(self):
        self.new_cash_desk.take_money({1: 2, 100: 3})
        self.assertFalse(self.new_cash_desk.can_withdraw_money(105))

if __name__ == '__main__':
    unittest.main()
