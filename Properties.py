from Location import location


class Properties(location):

    def __init__(self, name, color, price, rent, housecost, onehouse, twohouse, threehouse, fourhouse, hotel):
        super().__init__(name, "Property", price)
        self.rentChoices = [rent, onehouse, twohouse, threehouse, fourhouse, hotel]
        self.rent = rent
        self.houseHotelCost = housecost
        self.houses = 0
        self.color = color
        self.set = False

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def getRent(self, player):
        return self.rent

    def getHouseHotelCost(self):
        return self.houseHotelCost

    def addHouses(self, x):
        if not self.set:
            print("Set not completed")
            return
        for y in range(6):
            if self.rentChoices[y] == self.rent:
                if x + y > 5:
                    print("Too many houses trying to be placed")
                    return
                else:
                    self.rent = self.rentChoices[y+x]
                    self.houses += x
