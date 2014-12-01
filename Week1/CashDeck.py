class CashDeck():

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money_taken):
        for item in money_taken:
            self.money[item] += money_taken[item]

    def total(self):
        result = 0
        for key in self.money:
            result += key * self.money[key]
        return result

    def can_withdraw_money(self, money_for_withdraw):
        list_for_withdraw = []
        temp_money = 0
        for key in self.money:
            if self.money[key] > 0 and key <= money_for_withdraw:
                for i in range(0, self.money[key]):
                    list_for_withdraw.append(key)
        list_for_withdraw.sort(reverse=True)
        for items in list_for_withdraw:
            temp_money += items
            if temp_money > money_for_withdraw:
                temp_money -= items
            elif temp_money == money_for_withdraw:
                return True
        return False

