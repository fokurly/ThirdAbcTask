from source.HouseOfWisdom import HouseOfWisdom


class Riddle(HouseOfWisdom):
    """класс загадки"""

    def __init__(self, string, answer):
        HouseOfWisdom.__init__(self, string)
        self.answer = answer

    def output(self):
        return "Riddle: " + self.string + "\nThe answer on this riddle is: " + self.answer

