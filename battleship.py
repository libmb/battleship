# size of the board
from board import Board

ROWS = 6
COLS = 6
SIZE = 3
PLAYERS = 2

# Actual Game Starts Here
# =======================

# set up boards
player_boards = []
for i in range(PLAYERS):
    # create the boards
    player_boards.append(Board(ROWS, COLS))

for b in player_boards:
    # place the ships
    b.place_ship(SIZE)


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
                print("You got a hit!")
                break
            elif result == "Miss":
                print("You missed my battleship!")
                break
            elif result == "Sunk":
                print("You sunk my battleship. Player {}".format(whos_turn + 1))
                exit()
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
