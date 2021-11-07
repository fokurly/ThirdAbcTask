from source.HouseOfWisdom import HouseOfWisdom


class Aphorism(HouseOfWisdom):
    """Класс афоризм"""

    # конструктор
    def __init__(self, string, author):
        HouseOfWisdom.__init__(self, string)
        self.author = author

    def output(self):
        return "Aphorism: " + self.string + "\nThe author of this proverb: " + self.author
