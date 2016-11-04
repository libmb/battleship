from random import randint

# size of the board
ROWS = 5
COLS = 5

PLAYERS = 2

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


## Actual Game Starts Here
## =======================

# set up boards
boards = []
for i in range(PLAYERS):
    board = []
    for j in range(ROWS):
        board.append(["0"] * COLS)
    boards.append(board)

ship_locs = []
for i in range(PLAYERS):
    ship_row = random_row(boards[i])
    ship_col = random_col(boards[i])
    ship_locs.append((ship_row, ship_col))



print("Let's play Battleship!")
print_board(boards[0])

whos_turn = 0
while True:
    # set up turn
    location = ship_locs[whos_turn]
    ship_row = location[0]
    ship_col = location[1]
    board_to_check = boards[whos_turn]

    # allow player to guess.  repeat until guess is valid
    while True:
        guess_row = int(input("Player {} Guess Row: ".format(whos_turn + 1)))
        guess_col = int(input("Player {} Guess Col: ".format(whos_turn + 1)))
        if (guess_row < 0 or guess_row >= ROWS) or (guess_col < 0 or guess_col >= COLS):
            print("Oops, that's not even in the ocean. Guess again.")
        elif (board_to_check[guess_row][guess_col] == "X"):
            print("You guessed that one already. Guess again.")
        else:
            break

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship! Player {} wins!!!".format(whos_turn + 1))
        break # stops game
    else:
        print("You missed my battleship!")
        board_to_check[guess_row][guess_col] = "X"

    # print board for player
    print("Player {}'s board:'".format(whos_turn + 1))
    print_board(board_to_check)
    # change turns for next time in loop
    if whos_turn == PLAYERS - 1:
        whos_turn = 0
    else:
        whos_turn += 1

        
print("Goodbye")
