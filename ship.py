class Ship(object):
    def __init__(self, length, vertical, row, col):
        self.__length = length
        self.__vertical = vertical
        self.__peg_holes = [False] * length
        self.__ship_row = row
        self.__ship_col = col

    def ship_length(self):
        return self.__length

    def ship_start(self):
        return self.__ship_col

    def guess(self, row, col):
        # only works for horizontal ships
        if self.__ship_row is not row:
            return False
        if col >= self.__ship_col and col <= self.__ship_col + (self.__length-1):
            self.__peg_holes[col-self.__ship_col] = True
            return True
        return False


    def is_sunk(self):
        for p in self.__peg_holes:
            if not p:
                return False
        return True

