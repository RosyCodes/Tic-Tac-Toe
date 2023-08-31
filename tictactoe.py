# implemented using array / list
import random


# create the template for the board and cell numbers.
def startBoard():

    print(" TIC TAC TOE ")
    print("===============\n")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("\n===============")


# shows the current status of the board
def showboard():

    print(" TIC TAC TOE ")
    print("===============\n")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("-----------")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("\n===============")


# updates the board after a player makes a move
def updateboard(board, pos, char):
    board[pos] = char


# determines the next player
def nextMove(char):
    if char == "O":
        return "X"
    else:
        return "O"

# checks if there is a winning position after a move was made


def checkWinner(char):
    # checks the rows
    if ((board[1] == char) and (board[2] == char) and (board[3] == char)) or ((board[4] == char) and (board[5] == char) and (board[6] == char)) or ((board[7] == char) and (board[8] == char) and (board[9] == char)):
        return True
    # checks the columns
    elif ((board[1] == char) and (board[4] == char) and (board[7] == char)) or ((board[2] == char) and (board[5] == char) and (board[8] == char)) or ((board[3] == char) and (board[6] == char) and (board[9] == char)):
        return True
    # checks the diagonals
    elif ((board[1] == char) and (board[5] == char) and (board[9] == char)) or ((board[7] == char) and (board[5] == char) and (board[3] == char)):
        return True
    else:
        return False

# checks if the board is full


def checkFull():
    print("\nChecking empty cells . . .\n")
    if '' not in board:
        return True
    else:
        return False

# initializes the board to create empty cells


def initializeBoard():
    global board
    board = [''] * 10
    board[0] = '*'  # dummy or unused cell
    while True:
        startBoard()
        prompt = input("press RETURN KEY to start . . .")
        if not prompt:
            break
    print()

# determines the character (X or O) for each player


def assignPlayer(turn):
    print(f"\nPLAYER {turn} GOES FIRST!\n")
    print("-------------------------------")
    while True:
        player1 = input("Input your character [X/O]: ")
        player1 = player1.upper()
        if player1 == 'X' or player1 == 'O':
            break

    # assign the other character to player2
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    char = player1
    return char

# player takes turn in using cell numbers to place their character


def playGame(char):

    while True:
        print(f"\n{char}'s turn")
        try:
            pos = int(input("Assign to what cell? "))

            if pos < 1 or pos > 9:
                print("Cell address out of valid range.")
                continue

            if board[pos] != '':
                print("This cell is occupied. Try again.")
                continue

        except ValueError:
            print("Enter a number 1-9 only.")
            continue

        # calls the function to reflect the move
        updateboard(board, pos, char)

        # show current board status
        showboard()

        # check if the current move is a winner
        win_status = checkWinner(char)

        # check if the board is all occupied
        isFull = checkFull()

        if win_status == True:
            print(f"PLAYER {char} WINS!")
            break
        # check if all cells are empty for draw result
        elif isFull:
            print("Board is full! It's a draw!")
            break
        else:
            # this is the turn of the next player
            char = nextMove(char)


# MAIN BODY
while True:
    initializeBoard()
    showboard()

    # checks who will go first
    turn = random.randint(1, 2)

    # Player picks X or O
    char = assignPlayer(turn)

    # start the game and display the result
    playGame(char)
    again = input("Do you want to play again? Press N for No.")
    if again.upper() == "N":
        print("Goodbye!")
        break
