from random import randint

from ship import Ship


class Board(object):
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__ships = []
        self.__board = []
        for i in range(self.__rows):
            self.__board.append(["0"] * self.__cols)

    def __repr__(self):
        grid = ""
        for row in self.__board:
            grid += " ".join(row) + "\n"
        return grid

    def place_ship(self, ship_size):
        row = randint(0, len(self.__board) - 1)
        col = randint(0, len(self.__board[0]) - ship_size)
        self.__ships.append(Ship(ship_size, False, row, col))


    def guess(self, guess_row, guess_col):
        if self.__board[guess_row][guess_col] != "0":
            # check if we already guessed here
            return "Try again"

        for s in self.__ships:
            # check each ship for a hit
            if s.guess(guess_row, guess_col): # == True
                self.__board[guess_row][guess_col] = "H"
                if s.is_sunk(): # == True
                    for t in range(s.ship_start(), s.ship_start() + s.ship_length() -1):
                        self.__board[guess_row][t] = "="
                    return "Sunk"
                return "Hit"
        # no ships were hit, this is a miss. marks guess
        self.__board[guess_row][guess_col] = "X"
        return "Miss"
