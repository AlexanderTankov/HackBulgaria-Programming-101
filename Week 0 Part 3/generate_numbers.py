import sys
from random import randint


def main():
        filename = "%s" % sys.argv[0]
        file = open(filename, 'w')
        content = []
        for num in range(1, len(sys.argv[1])):
            content.append("%s" % randint(1, 1000))
        file.write(" ".join(content))
        file.close()
        file = open(filename, 'r')
        new_content = file.read()
        print(new_content)
        print(' ')
        file.close()
if __name__ == '__main__':
    main()
