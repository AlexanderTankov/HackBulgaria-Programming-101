import sys


def main():
    for arg in range(1, len(sys.argv)):
        filename = "%s" % sys.argv[arg]
        file = open(filename, 'r')
        content = file.read()
        print(content)
        print('\n')
        file.close()
if __name__ == '__main__':
    main()
