class location:

    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def __str__(self):
        return self.name
