def calculate_coins(sum):
    coins = {"100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0}
    temp_list = [100, 50, 20, 10, 5, 2, 1]
    sum *= 100
    while sum != 0:
        temp = sum
        for price in temp_list:
            if (sum - price) >= 0:
                coins["%s" % price] += 1
                sum -= price
                if sum != temp:
                    break
    return coins
