from nth_fib_lists import nth_fib_lists

def member_of_nth_fib_lists(listA, listB, needle):
    temp = 0
    fib_list = []
    while len(fib_list) < len(needle):
        temp += 1
        fib_list = nth_fib_lists(listA, listB, temp)
    return fib_list == needle
