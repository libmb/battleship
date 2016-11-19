from random import randint

# size of the board
ROWS = 5
COLS = 6

PLAYERS = 2


class Board(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []
        self.ship_row = -1
        self.ship_col = -1
        for i in range(self.rows):
            self.board.append(["0"] * self.cols)

    def __repr__(self):
        grid = ""
        for row in self.board:
            grid += " ".join(row) + "\n"
        return grid

    def place_ship(self):
        self.ship_row = randint(0, len(self.board)-1)
        self.ship_col = randint(0, len(self.board[0])-1)

    def guess(self, guess_row, guess_col):
        if guess_row == self.ship_row and guess_col == self.ship_col:
            return "Hit"
        elif self.board[guess_row][guess_col] == "X":
            return "Try again"
        else:
            self.board[guess_row][guess_col] = "X"
            return "Miss"


# Actual Game Starts Here
# =======================

# set up boards
player_boards = []
for i in range(PLAYERS):
    # create the boards
    player_boards.append(Board(ROWS, COLS))

for b in player_boards:
    # place the ships
    b.place_ship()


print("Let's play Battleship!")
print(player_boards[0])

whos_turn = 0
while True:
    # set up turn
    board_to_check = player_boards[whos_turn]

    # allow player to guess.  repeat until guess is valid
    while True:
        guess_row = int(input("Player {} Guess Row: ".format(whos_turn + 1)))
        guess_col = int(input("Player {} Guess Col: ".format(whos_turn + 1)))
        if (guess_row < 0 or guess_row >= ROWS) or (guess_col < 0 or guess_col >= COLS):
            print("Oops, that's not even in the ocean. Guess again.")
        else:
            result = board_to_check.guess(guess_row, guess_col)
            if result == "Hit":
                print("Congratulations! You sunk my battleship! Player {} wins!!!".format(whos_turn + 1))
                exit()
            elif result == "Miss":
                print("You missed my battleship!")
                break
            else:
                print("You already guess that. Try Again")

    # print board for player
    print("Player {}'s board:'".format(whos_turn + 1))
    print(board_to_check)
    # change turns for next time in loop
    if whos_turn == PLAYERS - 1:
        whos_turn = 0
    else:
        whos_turn += 1

        
print("Goodbye")
