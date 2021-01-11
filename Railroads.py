from Location import location


class Railroads(location):

    def __init__(self, name):
        super().__init__(name, "Railroad", 200)
        self.rent = 25
        self.rentChoices = [25, 50, 100, 200]
        self.numOfRR = 0

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def getRent(self):
        count = 0
        for x in player.properties:
            if x.getType() == "Railroad":
                count += 1
        self.rent = self.rentChoices[count]
        return self.rent
