import random
from Location import location

class utility(location):

    def __init__(self, name):
        super().__init__(name, "Utility", 150)
        self.both = False

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def getRent(self, player):
        diceRoll = random.randint(1, 6)
        print("The dice roll for the payment is " + str(diceRoll))
        if self.both:
            rent = diceRoll * 10
        else:
            rent = diceRoll * 4
        return rent
