from random import randint

# size of the board
ROWS = 5
COLS = 5

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


## Actual Game Starts Here
## =======================

# set up board
player1board = []
player2board = []
for i in range(ROWS):
    player1board.append(["O"] * COLS)
    player2board.append(["O"] * COLS)

ship_row_p1 = random_row(player1board)
ship_col_p1 = random_col(player1board)
ship_row_p2 = random_row(player2board)
ship_col_p2 = random_col(player2board)



print("Let's play Battleship!")
print_board(player1board)

whos_turn = 1
while True:
    # set up turn
    if whos_turn == 1:
        ship_row = ship_row_p1
        ship_col = ship_col_p1
        board_to_check = player1board
    else:
        ship_row = ship_row_p2
        ship_col = ship_col_p2
        board_to_check = player2board

    # allow player to guess.  repeat until guess is valid
    while True:
        guess_row = int(input("Player {} Guess Row: ".format(whos_turn)))
        guess_col = int(input("Player {} Guess Col: ".format(whos_turn)))
        if (guess_row < 0 or guess_row >= ROWS) or (guess_col < 0 or guess_col >= COLS):
            print("Oops, that's not even in the ocean. Guess again.")
        elif (board_to_check[guess_row][guess_col] == "X"):
            print("You guessed that one already. Guess again.")
        else:
            break

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship! Player {} wins!!!".format(whos_turn))
        break # stops game
    else:
        print("You missed my battleship!")
        board_to_check[guess_row][guess_col] = "X"

    # print board for player
    print("Player {}'s board:'".format(whos_turn))
    print_board(board_to_check)
    # change turns for next time in loop        
    if whos_turn == 1:
        whos_turn = 2
    else:
        whos_turn = 1
        
print("Goodbye")
