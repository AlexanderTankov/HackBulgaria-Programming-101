class CashDeck():
    def __init__(self, money={100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money

    def take_money(self, money_taken):
        for item in money_taken:
            self.money[item] += money_taken[item]

    def total(self):
        result = 0
        for key in self.money:
            if self.money[key] != 0:
                for time in range(0, self.money[key]):
                    result += key
        return result

    def can_withdraw_money(self, money_for_withdraw):
        list_for_withdraw = []
        for key in self.money:
            if self.money[key] != 0:
                list_for_withdraw.append([key, self.money[key]])
        list_for_withdraw = CashDeck.sort_list(list_for_withdraw)
        temp_money = money_for_withdraw
        for items in list_for_withdraw:
            if temp_money > items[0]:
                temp_money -= items[0]
                print(items[0])
                print(items[1])
                if items[1] == 1:
                    list_for_withdraw.remove(items)
                else:
                    items[1] -= 1
        print(temp_money)
        print(list_for_withdraw)

    @staticmethod
    def sort_list(list_for_sort):
        result = []
        while len(list_for_sort) != 1:
            max_elem = list_for_sort[0][0]
            pos_max_elem = 0
            for elem in range(1, len(list_for_sort)):
                moment_elem = list_for_sort[elem][0]
                if moment_elem > max_elem:
                    max_elem = moment_elem
                    pos_max_elem = elem
            result.append([list_for_sort[pos_max_elem][0], list_for_sort[pos_max_elem][1]])
            del list_for_sort[pos_max_elem]
        result.append(list_for_sort[0])
        return result


my_cach_desk = CashDeck()
my_cach_desk.take_money({1: 2, 50: 1, 20: 1})
print(my_cach_desk.total())
#my_cach_desk.can_withdraw_money(30) #False
my_cach_desk.can_withdraw_money(70) #True
