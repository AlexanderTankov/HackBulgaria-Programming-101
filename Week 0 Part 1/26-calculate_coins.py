def calculate_coins(sum):
    coins = {"1", "2", "100", "5", "10", "50", "20"}
    for key in coins:
        key = 0
    sum *= 100
    while sum != 0:
        temp = sum
        if sum - 100 >= 0:
            coins["100"] += 1
        for coin in coins:
            if sum - int(coin) >= 0:
                sum -= int(coin)
            if sum != temp:
                break
    return coins


print(calculate_coins(0.53))
print(calculate_coins(8.94))
