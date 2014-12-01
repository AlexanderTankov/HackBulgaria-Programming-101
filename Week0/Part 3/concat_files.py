import sys
import os


def main():
    if not os.path.isfile("MEGATRON.txt"):
        t_file = open("MEGATRON.txt", 'w')
        t_file.close()
    temp_file = open("MEGATRON.txt", 'r')
    content = temp_file.read()
    temp_file.close()
    big_file = open("MEGATRON.txt", 'w')
    filename = "%s" % sys.argv[1]
    file = open(filename, 'r')
    new_content = content + '\n' + file.read() + '\n'
    file.close()
    for arg in range(2, len(sys.argv)):
        filename = "%s" % sys.argv[arg]
        temp_file = open(filename, 'r')
        new_content += temp_file.read() + '\n'
        temp_file.close()
    big_file.write("".join(new_content))
    big_file.close()
    temp_file = open("MEGATRON.txt", 'r')
    content = temp_file.read()
    print(content)
    temp_file.close()

if __name__ == '__main__':
    main()
