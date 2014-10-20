class CashDeck():
  
    def __init__(self, money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money

    def take_money(self, money_taken):
        for item in money_taken:
            self.money[item] += money_taken[item]

    def total(self):
        sum = 0
        for item in self.money:
            sum += self.money[item]*item
        return sum

    def can_withdraw_money(self, amount_of_money):
        my_list = []
        result = 0
        for item in self.money:
            if self.money[item] > 0 and item <= amount_of_money:
                #print ("self_money.item {}".format(self.money[item]))
                for i in range(0, self.money[item]):
                    my_list.append(item)
        my_list.sort(reverse = True)
        #print (my_list)
        for item in my_list:
            result += item
            #print (result)
            if result > amount_of_money:
                result -= item
            elif result == amount_of_money:
                return True
        return False




my_cash_deck = CashDeck()
print (my_cash_deck.money)
#print (my_cash_deck.money)
print (my_cash_deck.take_money({1: 2, 100: 3}))
print (my_cash_deck.money)
print (my_cash_deck.total())
print (my_cash_deck.can_withdraw_money(19))
