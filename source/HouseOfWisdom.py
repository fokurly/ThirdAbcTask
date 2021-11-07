class HouseOfWisdom:
    """класс кладезь мудрости"""

    # конструктор
    def __init__(self, string):
        self.string = string

    def get_mean(self):
        mean = 0
        for i in self.string:
            if (i == '.' or i == ' ' or i == ',' or i == '!' or i == ';'
                    or i == ':' or i == '/'):
                mean += 1

        return mean
