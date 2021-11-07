from source.HouseOfWisdom import HouseOfWisdom


class Proverb(HouseOfWisdom):
    """класс пословица"""

    # констрктор
    def __init__(self, string, country):
        HouseOfWisdom.__init__(self, string)
        self.country = country

    def output(self):
        return "Proverb: " + self.string + "\nThe country of this proverb is: " + self.country
