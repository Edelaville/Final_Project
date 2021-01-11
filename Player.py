from Piece import pieces


class Player:
    def __init__(self):
        self.name = input("Please pick a piece from the options above.")
        self.piece = pieces(self.name)
        self.balance = 2500
        self.properties = []

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def changeBalance(self, amount):
        self.balance += amount
        return self.balance

    def getProperties(self):
        return self.properties

    def addToList(self, change):
        self.properties.append(change.getName())
        return self.properties

    def getPiece(self):
        return self.piece
