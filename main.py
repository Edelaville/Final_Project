from Board import board
from Piece import pieces
from Player import Player

b1 = board()
b1.setUpBoard()
b1.printBoard()
print("")

piece_options = ["dog", "hat", "car", "ship", "wheelbarrow", "shoe"]
print(piece_options)


p1 = Player()
piece_options.remove(p1.getName())
print("")
print(piece_options)


p2 = Player()
piece_options.remove(p2.getName())
print("")
print(piece_options)


p3 = Player()
piece_options.remove(p3.getName())
print("")
print(piece_options)


p4 = Player()
piece_options.remove(p4.getName())
print("")


win = False
while not win:
    print("Player 1's Turn")
    print("Player 1's Balance before their turn is " + str(p1.getBalance()))
    print("Player 1's Property list before their turn is " + str(p1.getProperties()))
    pos = b1.moveOnBoard(p1)
    print("Player 1 landed on " + str(b1.returnSpace(pos[0], pos[1])))
    location_type = b1.returnSpace(pos[0], pos[1]).getType()
    price = b1.returnSpace(pos[0], pos[1]).getPrice()
    if p2.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
        if p3.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
            if p4.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
                if location_type == "ChanceChest":
                    chance = b1.returnSpace(pos[0], pos[1]).getChance()
                    b1.returnSpace(pos[0], pos[1]).analyzeChance(chance, p1)
                print(location_type)
                print(price)
                if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
                    buy = input("Would you like to purchase " + str(b1.returnSpace(pos[0], pos[1])) + " for $" + str(
                        price) + " (Yes or No)")
                    if buy == "Yes":
                        p1.changeBalance((-1) * price)
                        p1.addToList(b1.returnSpace(pos[0], pos[1]))
    if p2.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p2)
            p1.changeBalance((-1) * rent)
            p2.changeBalance(rent)
            print("Player 1 pays PLayer 2 $" + str(rent) + " for rent")
    elif p3.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p3)
            p1.changeBalance((-1) * rent)
            p3.changeBalance(rent)
            print("Player 1 pays PLayer 3 $" + str(rent) + " for rent")
    elif p4.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p4)
            p1.changeBalance((-1) * rent)
            p4.changeBalance(rent)
            print("Player 1 pays PLayer 4 $" + str(rent) + " for rent")
    print("Player 1's Balance after their turn is " + str(p1.getBalance()))
    print("Player 1's Property list after their turn is " + str(p1.getProperties()))
    print("")

    print("Player 2's Turn")
    print("Player 2's Balance after their turn is " + str(p2.getBalance()))
    print("Player 2's Property list after their turn is " + str(p2.getProperties()))
    pos = b1.moveOnBoard(p2)
    print("Player 2 landed on " + str(b1.returnSpace(pos[0], pos[1])))
    location_type = b1.returnSpace(pos[0], pos[1]).getType()
    price = b1.returnSpace(pos[0], pos[1]).getPrice()
    if p1.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
        if p3.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
            if p4.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
                if location_type == "ChanceChest":
                    chance = b1.returnSpace(pos[0], pos[1]).getChance()
                    b1.returnSpace(pos[0], pos[1]).analyzeChance(chance, p2)
                print(location_type)
                print(price)
                if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
                    buy = input("Would you like to purchase " + str(b1.returnSpace(pos[0], pos[1])) + " for $" + str(
                        price) + " (Yes or No)")
                    if buy == "Yes":
                        p2.changeBalance((-1) * price)
                        p2.addToList(b1.returnSpace(pos[0], pos[1]))
    if p1.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p1)
            p2.changeBalance((-1) * rent)
            p1.changeBalance(rent)
            print("Player 2 pays PLayer 1 $" + str(rent) + " for rent")
    elif p3.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p3)
            p2.changeBalance((-1) * rent)
            p3.changeBalance(rent)
            print("Player 2 pays PLayer 3 $" + str(rent) + " for rent")
    elif p4.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p4)
            p2.changeBalance((-1) * rent)
            p4.changeBalance(rent)
            print("Player 2 pays PLayer 4 $" + str(rent) + " for rent")
    print("Player 2's Balance after their turn is " + str(p2.getBalance()))
    print("Player 2's Property list after their turn is " + str(p2.getProperties()))
    print("")

    print("Player 3's Turn")
    print("Player 3's Balance after their turn is " + str(p3.getBalance()))
    print("Player 3's Property list after their turn is " + str(p3.getProperties()))
    pos = b1.moveOnBoard(p3)
    print("Player 3 landed on " + str(b1.returnSpace(pos[0], pos[1])))
    location_type = b1.returnSpace(pos[0], pos[1]).getType()
    price = b1.returnSpace(pos[0], pos[1]).getPrice()
    if p1.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
        if p2.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
            if p4.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
                if location_type == "ChanceChest":
                    chance = b1.returnSpace(pos[0], pos[1]).getChance()
                    b1.returnSpace(pos[0], pos[1]).analyzeChance(chance, p3)
                print(location_type)
                print(price)
                if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
                    buy = input("Would you like to purchase " + str(b1.returnSpace(pos[0], pos[1])) + " for $" + str(
                        price) + " (Yes or No)")
                    if buy == "Yes":
                        p3.changeBalance((-1) * price)
                        p3.addToList(b1.returnSpace(pos[0], pos[1]))
    if p1.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p1)
            p3.changeBalance((-1) * rent)
            p1.changeBalance(rent)
            print("Player 3 pays PLayer 1 $" + str(rent) + " for rent")
    elif p2.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p2)
            p3.changeBalance((-1) * rent)
            p2.changeBalance(rent)
            print("Player 3 pays PLayer 2 $" + str(rent) + " for rent")
    elif p4.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p4)
            p3.changeBalance((-1) * rent)
            p4.changeBalance(rent)
            print("Player 3 pays PLayer 4 $" + str(rent) + " for rent")
    print("Player 3's Balance after their turn is " + str(p3.getBalance()))
    print("Player 3's Property list after their turn is " + str(p3.getProperties()))
    print("")

    print("Player 4's Turn")
    print("Player 4's Balance after their turn is " + str(p4.getBalance()))
    print("Player 4's Property list after their turn is " + str(p4.getProperties()))
    pos = b1.moveOnBoard(p4)
    print("Player 1 landed on " + str(b1.returnSpace(pos[0], pos[1])))
    location_type = b1.returnSpace(pos[0], pos[1]).getType()
    price = b1.returnSpace(pos[0], pos[1]).getPrice()
    if p1.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
        if p2.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
            if p3.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) == 0:
                if location_type == "ChanceChest":
                    chance = b1.returnSpace(pos[0], pos[1]).getChance()
                    b1.returnSpace(pos[0], pos[1]).analyzeChance(chance, p4)
                print(location_type)
                print(price)
                if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
                    buy = input("Would you like to purchase " + str(b1.returnSpace(pos[0], pos[1])) + " for $" + str(
                        price) + " (Yes or No)")
                    if buy == "Yes":
                        p4.changeBalance((-1) * price)
                        p4.addToList(b1.returnSpace(pos[0], pos[1]))
    if p1.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p1)
            p4.changeBalance((-1) * rent)
            p1.changeBalance(rent)
            print("Player 4 pays PLayer 1 $" + str(rent) + " for rent")
    elif p2.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p2)
            p4.changeBalance((-1) * rent)
            p2.changeBalance(rent)
            print("Player 4 pays PLayer 2 $" + str(rent) + " for rent")
    elif p3.getProperties().count(str(b1.returnSpace(pos[0], pos[1]))) > 0:
        if location_type == "Property" or location_type == "Utility" or location_type == "Railroad":
            rent = b1.returnSpace(pos[0], pos[1]).getRent(p3)
            p4.changeBalance((-1) * rent)
            p3.changeBalance(rent)
            print("Player 4 pays PLayer 3 $" + str(rent) + " for rent")
    print("Player 4's Balance after their turn is " + str(p4.getBalance()))
    print("Player 4's Property list after their turn is " + str(p4.getProperties()))
    print("")

