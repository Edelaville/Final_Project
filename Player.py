from Piece import pieces
class Player:
    def __init__(self, piece):
        name = input("Which piece would you like?")
        self.piece = pieces()
        self.balance = 2000
        self.properties = []
