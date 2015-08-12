from time import gmtime, strftime, sleep, clock
from random import randint
from functools import wraps
from os import listdir
from os.path import isfile, join
from os import getcwd

# Task 1


def accepts(*types):
    def accepter(func):
        def accept(*names):
            if len(types) != len(names):
                raise TypeError()

            for t in range(0, len(types)):
                for n in range(0, len(names)):
                    if type(names[n]) != types[t]:
                        raise TypeError("Argument {} of {} is not {}!".format
                                        ((n + 1),
                                         func.__name__,
                                         types[t].__name__)
                                        )

            return func(*names)
        return accept
    return accepter


@accepts(str)
def say_hallo(name):
    return "Hello, I am {}".format(name)

# print(say_hallo("asd"))


# Task 2
def caesar_cipher(sentence, num):
    result = ""
    for char in sentence:
        result += chr(ord(char) + num)
    return result


def encrypt(num):
    def encrypter(func):
        @wraps(func)
        def encrypting():
            return caesar_cipher(func(), num)
        return encrypting
    return encrypter

# @encrypt(2)
#  def get_low():
#     return "Get get get low"
# 
#  print(get_low())


# Task 3
def log(file_name):
    def loger(func):
        @wraps(func)
        def logs():
            my_file = open(file_name, 'a')
            my_file.write("{} was called at {}\n".format(
                func.__name__,
                strftime(
                    "%Y-%m-%d %H:%M:%S",
                    gmtime())
            )
            )
            my_file.close()
            return func
        return logs
    return loger


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

# get_low()


# Task 4
def performance(file_name):
    def performer(func):
        @wraps(func)
        def performances():
            start = clock()
            result = func()
            elapsed = clock()
            elapsed = elapsed - start
            my_file = open(file_name, 'a')
            my_file.write("{} was called and took {} seconds to compleat\n".format(
                func.__name__,
                elapsed*1000.0
            )
            )
            my_file.close()
            return result
        return performances
    return performer


@performance('log.txt')
def something_heavy():
    sleep(randint(1, 10))
    return "I am done!"

# something_heavy()

# Task 5


def memorize(func):
    fib_nums = {}

    def memorizes(num):
        if num not in fib_nums:
            fib_nums[num] = func(num)
        return fib_nums[num]
    return memorizes


@memorize
def fib(n):
    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)

# print(fib(50))


# Day 2
# Task 1
def chain(iterable_one, iterable_two):
    for i in iterable_one:
        yield i
    for ii in iterable_two:
        yield ii


# Task 2
# print(list(chain(range(0, 4), range(4, 8))))
def compress(iterable, mask):
    result = zip(iterable, mask)
    for i, p in result:
        if p:
            yield i

# print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))


# Task 3
def cycle(iterable):
    while True:
        for i in iterable:
            yield i

# endless = cycle(range(0, 10))
# for item in endless:
#     print(item)


def filter_list(my_list):
    result = []
    for my_str in my_list:
        if my_str[-4::] == '.txt':
            result.append(my_str)
    return result


def bookReader():
    onlyfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
    onlyfiles = filter_list(onlyfiles)
    onlyfiles.sort()
    for name in onlyfiles:
        with open(name, "r") as f:
            my_str = f.readline()
            for line in f:
                if len(line) > 1 and line[0] == '#' and line[1] == ' ':
                    yield my_str
                    my_str = line
                else:
                    my_str += line
            yield my_str


bookReader = bookReader()
for i in bookReader:
    print(i)
