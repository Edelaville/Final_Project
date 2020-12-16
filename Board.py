from Location import location
from Properties import Properties
from Utility import utility
from ChanceChest import ChanceChest
from Railroads import Railroads


class board:
    def __init__(self):
        self.board = []
        self.board.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        for x in range(9):
            self.board.append([" ", "X", "X", "X", "X", "X", "X", "X", "X", "X", " "])
        self.board.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

    def printBoard(self):
        for x in self.board:
            print(x)

    def editBoard(self, x, y, change):
        self.board[x][y] = change

    def setUpBoard(self):
        self.board[0][0] = location("GO", "Start", 0)
        self.board[0][1] = Properties("Mediterranean Avenue", "Brown", 60, 2, 50, 10, 30, 90, 160, 250)
        self.board[0][2] = ChanceChest("Community Chest")
        self.board[0][3] = Properties("Baltic Avenue", "Brown", 60, 4, 50, 20, 60, 180, 320, 500)
        self.board[0][4] = location("Income Tax", "Tax", 200)
        self.board[0][5] = Railroads("Reading Railroad")
        self.board[0][6] = Properties("Oriental Avenue", "Light Blue", 100, 6, 50, 30, 90, 270, 400, 550)
        self.board[0][7] = ChanceChest("Chance")
        self.board[0][8] = Properties("Vermont Avenue", "Light Blue", 100, 6, 50, 30, 90, 270, 400, 550)
        self.board[0][9] = Properties("Connecticut Avenue", "Light Blue", 120, 8, 50, 40, 100, 300, 450, 600)
        self.board[0][10] = location("Jail", "Jail", 0)
        self.board[1][10] = Properties("St Charles Place", "Pink", 140, 10, 100, 50, 150, 450, 625, 750)
        self.board[2][10] = utility("Electric Company")
        self.board[3][10] = Properties("States Avenue", "Pink", 140, 10, 100, 50, 150, 450, 625, 750)
        self.board[4][10] = Properties("Virginia Avenue", "Pink", 160, 12, 100, 60, 180, 500, 700, 900)
        self.board[5][10] = Railroads("Pennsylvania Railroad")
        self.board[6][10] = Properties("St James Place", "Orange", 180, 14, 100, 70, 200, 550, 750, 950)
        self.board[7][10] = ChanceChest("Community Chest")
        self.board[8][10] = Properties("Tennessee Avenue", "Orange", 180, 14, 100, 70, 200, 550, 750, 950)
        self.board[9][10] = Properties("New York Avenue", "Orange", 200, 16, 100, 80, 220, 600, 800, 1000)

        self.board[10][10] = location("Free Parking", "Start", 0)
        self.board[10][9] = Properties("Kentucky Avenue", "Red", 220, 18, 150, 90, 250, 700, 875, 1050)
        self.board[10][8] = ChanceChest("Chance")
        self.board[10][7] = Properties("Indiana Avenue", "Red", 220, 18, 150, 90, 250, 700, 875, 1050)
        self.board[10][6] = Properties("Illinois Avenue", "Red", 240, 20, 150, 100, 300, 750, 925, 1100)
        self.board[10][5] = Railroads("B&O Railroad")
        self.board[10][4] = Properties("Atlantic Avenue", "Yellow", 260, 22, 150, 110, 330, 800, 975, 1150)
        self.board[10][3] = Properties("Ventnor Avenue", "Yellow", 260, 22, 150, 110, 330, 800, 975, 1150)
        self.board[10][2] = utility("Water Works")
        self.board[10][1] = Properties("Marvin Gardens", "Yellow", 280, 24, 150, 120, 360, 850, 1025, 1200)
        self.board[10][0] = location("Go to jail", "Jail", 0)
        self.board[9][0] = Properties("Pacific Avenue", "Green", 300, 26, 200, 130, 390, 900, 1100, 1275)
        self.board[8][0] = Properties("North Carolina Avenue", "Green", 300, 26, 200, 130, 390, 900, 1100, 1275)
        self.board[7][0] = ChanceChest("Community Chest")
        self.board[6][0] = Properties("Pennsylvania Avenue", "Green", 320, 28, 200, 150, 450, 1000, 1200, 1400)
        self.board[5][0] = Railroads("Short Line")
        self.board[4][0] = ChanceChest("Chance")
        self.board[3][0] = Properties("Park Place", "Dark Blue", 350, 35, 200, 175, 500, 1100, 1300, 1500)
        self.board[2][0] = location("Luxury Tax", "Tax", 100)
        self.board[1][0] = Properties("Boardwalk", "Dark Blue", 400, 50, 200, 200, 600, 1400, 1700, 2000)
