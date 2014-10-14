import sys


def main():
    filename = "%s" % sys.argv[2]
    file = open(filename, 'r')
    new_content = file.read()
    if sys.argv[1] == "chars":
        print(len(new_content) - 1)
    elif sys.argv[1] == "words":
        count_words = 1
        for chars in range(0, len(new_content) - 1):
            if new_content[chars] == " " or (new_content[chars] == "\n" and new_content[chars + 1] != "\n"):
                count_words += 1
        print(count_words)
    elif sys.argv[1] == "lines":
        count_lines = 0
        for chars in range(0, len(new_content)):
            if new_content[chars] == "\n":
                count_lines += 1
        print(count_lines)
    file.close()
if __name__ == '__main__':
    main()
