# -------Global Variables------


# Board Game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If the game is still going
game_still_going = True

# who won or Tie
winner = None

# whose turn is it
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    global winner

    # Display Initial Board
    display_board()

    while game_still_going:
        # handle the turn of the players
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

        # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    else:
        winner = None
        print(" Tie.")


def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1-9 : ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9 : ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go Again")

    board[position] = player

    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # set up global variable+
    global winner

    # checkrows
    row_winner = check_rows()
    # check_cols
    col_winner = check_cols()
    # check diagonals
    diag_winner = check_diag()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
    return


def check_rows():
    # set up global variable
    global game_still_going

    # check that rows have same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    # return the winner (X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[1]
    if row_3:
        return board[2]
    return


def check_cols():
    # set up global variable
    global game_still_going

    # check that cols have same value
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going = False

    # return the winner (X or O)
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return


def check_diag():
    # set up global variable
    global game_still_going

    # check that diag have same value
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    if diag_1 or diag_2:
        game_still_going = False

    # return the winner (X or O)
    if diag_1:
        return board[0]
    if diag_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # global variables needed
    global current_player
    # if the player is X , change it to O
    if current_player == "X":
        current_player = "O"
    # if the player is O, change it to X
    elif current_player == "O":
        current_player = "X"

    return


play_game()

# board
# display board
# play game
# handles turn
# check win
# check rows
# check columns
# check diagonals
# check tie
# flip player
