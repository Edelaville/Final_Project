class board:
    def __init__(self):
        self.board = []
        self.board.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        for x in range(8):
            self.board.append([" ", "X", "X", "X", "X", "X", "X", "X", "X", "X", " "])
        self.board.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

    def printBoard(self):
        # Traverses the Y-values
        for x in self.board:
            print(x)

    def setUpBoard(self):
        yield
