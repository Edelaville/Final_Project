from Location import location
import random


class ChanceChest(location):

    def __init__(self, name):
        super().__init__(name, "ChanceChest", 0)
        self.chance = ["Advance to GO", "Advance to Illinois Ave", "Advance to St Charles Place",
                       "Advance to nearest utility and pay 10x the dice roll",
                       "Advance to nearest railroad and pay double the rent",
                       "Bank pays you $50", "Get Out of Jail Free", "Get Out of Jail Free",
                       "Go directly to jail", "Take a trip to Reading Railroad", "Take a trip to Boardwalk",
                       "Won a crossword Puzzle - Collect $100", "Bank error in your favor - Collect $200",
                       "Doctors fee - Pay $50", "Go back three spaces", "Go back three spaces"]

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getChance(self):
        length = len(self.chance)
        x = random.randint(1, length-1)
        return self.chance[x]
