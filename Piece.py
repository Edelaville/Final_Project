class pieces:
    def __init__(self, type):
        piece_types = ["dog", "hat", "car", "ship", "wheelbarrow", "shoe"]
        self.valid = False
        for x in piece_types:
            if type == x:
                self.valid = True
                piece_types.remove(type)
        self.type = type
        self.position = [0, 0]
        self.row_coef = 0
        self.col_coef = 1

    def move(self):
        if self.position[0] == 0 and self.position[1] == 0:
            self.row_coef = 0
            self.col_coef = 1

        if self.position[0] == 0 and self.position[1] == 10:
            self.row_coef = 1
            self.col_coef = 0

        if self.position[0] == 10 and self.position[1] == 10:
            self.row_coef = 0
            self.col_coef = -1

        if self.position[0] == 10 and self.position[1] == 0:
            self.row_coef = -1
            self.col_coef = 0

        self.position[0] += 1 * self.row_coef
        self.position[1] += 1 * self.col_coef
