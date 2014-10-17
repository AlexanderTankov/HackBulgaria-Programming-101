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


def member_of_nth_fib_lists(listA, listB, needle):
    temp = 0
    fib_list = []
    while len(fib_list) < len(needle):
        temp += 1
        fib_list = nth_fib_lists(listA, listB, temp)
    return fib_list == needle

print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
print(member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
print(member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
print(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))
