def nth_fib_lists(listA, listB, n):
    if listA == [] and listB == []:
        return []
    if n == 0:
        return []
    elif n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        return nth_fib_lists(listA, listB, n - 2) + nth_fib_lists(listA, listB, n - 1)


def nth_fib_lists_snd(listA, listB, n):
    a = listB
    result = listA + listB
    if n == 0:
        return []
    elif n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        for digit in range(3, n):
            b = result
            result = a + b
            a = b
    return result
