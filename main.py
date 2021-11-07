import sys
from random import *
from source.Container import Container


def get_size():
    with open(sys.argv[2]) as f:
        text = f.readline()
        return text


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Неверные входные параметры")
    else:
        if sys.argv[1] == '-i':
            container = Container(get_size())
            container.read_file()
            container.output(sys.argv[3])
            container.sort_list()
            container.output(sys.argv[4])
        elif sys.argv[1] == '-r':
            container = Container(randint(1, 100))
            container.random_input()
            container.output(sys.argv[3])
            container.sort_list()
            container.output(sys.argv[4])
