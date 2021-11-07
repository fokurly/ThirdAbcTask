import sys
from random import *
from source.Aphorism import Aphorism
from source.Proverb import Proverb
from source.Riddle import Riddle


class Container:

    def __init__(self, size):
        self.size = int(size)
        self.list = []

    def read_file(self):
        with open(sys.argv[2]) as f:
            print(f.readline())
            for i in range(self.size):
                wisdom_type = int(f.readline())
                string = f.readline()
                mean = f.readline()

                if wisdom_type == 1:
                    riddle = Riddle(string, mean)
                    self.list.append(riddle)
                elif wisdom_type == 2:
                    aphorism = Aphorism(string, mean)
                    self.list.append(aphorism)
                elif wisdom_type == 3:
                    proverb = Proverb(string, mean)
                    self.list.append(proverb)
                else:
                    print("Incorrect type")

    @staticmethod
    def get_word(self, num_of_word):
        with open(sys.argv[2]) as f:
            for i in range(num_of_word):
                f.readline()

            return f.readline()

    @staticmethod
    def generate_string(self):
        length_of_string = randint(1, 25)
        temp = ""
        for j in range(length_of_string):
            temp += self.get_word(self, randint(1, 2184))

        tempList = temp.splitlines()
        temp = ""
        for word in tempList:
            temp += word + " "

        return str(temp)

    def random_input(self):
        with open(sys.argv[2]) as f:
            for i in range(self.size):
                wisdom_type = randint(1, 3)
                string = self.generate_string(self)
                mean = self.get_word(self, randint(1, 2184))

                if wisdom_type == 1:
                    riddle = Riddle(string, mean)
                    self.list.append(riddle)
                elif wisdom_type == 2:
                    aphorism = Aphorism(string, mean)
                    self.list.append(aphorism)
                elif wisdom_type == 3:
                    proverb = Proverb(string, mean)
                    self.list.append(proverb)
                else:
                    print("Incorrect type")

    def output(self, file_name):
        with open(file_name, 'w') as f:
            f.write("The size of container is: " + str(self.size) + "\n")
            for i in range(self.size):
                f.write("------------------------\n")
                f.write(self.list[i].output())
                f.write("Meaning: " + str(self.list[i].get_mean()) + "\n")

    def sort_list(self):
        for i in range(self.size):
            for j in range(self.size - i - 1):
                if self.list[j].get_mean() > self.list[j+1].get_mean():
                    temp = self.list[j]
                    self.list[j] = self.list[j+1]
                    self.list[j+1] = temp
