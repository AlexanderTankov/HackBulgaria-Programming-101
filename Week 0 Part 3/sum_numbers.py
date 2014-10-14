import sys
from random import randint


def sum_of_int_in_str(str):
    result = int(str[0])
    for char in range(0, len(str)):
        if str[char] == " ":
            result += int(str[char + 1])
    return result


def main():
        filename = "%s" % sys.argv[1]
        file = open(filename, 'r')
        new_content = file.read()
        print(sum_of_int_in_str(new_content))
        file.close()
if __name__ == '__main__':
    main()
