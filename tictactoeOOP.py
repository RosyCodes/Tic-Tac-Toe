import random


class TicTacToe:
    def __init__(self):
        self.player = ''
        self.board = [''] * 10
        self.board[0] = '*'

    @staticmethod
    def startBoard():  # show the board with cell assignment
        print(" TIC TAC TOE ")
        print("===============\n")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\n===============")

    def showboard(self):  # shows the placement of the list elements
        print("\n TIC TAC TOE ")
        print("===============\n")
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
        print("-----------")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print("-----------")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")
        print("\n===============")

    def updateboard(self, board, pos, char):  # updates
        self.board[pos] = char

    # determines the next player
    def nextMove(self, char):
        if char == "O":
            return "X"
        else:
            return "O"

    def checkWinner(self, char):
        # checks the rows
        if ((self.board[1] == char) and (self.board[2] == char) and (self.board[3] == char)) or ((self.board[4] == char) and (self.board[5] == char) and (self.board[6] == char)) or ((self.board[7] == char) and (self.board[8] == char) and (self.board[9] == char)):
            return True
        # checks the columns
        elif ((self.board[1] == char) and (self.board[4] == char) and (self.board[7] == char)) or ((self.board[2] == char) and (self.board[5] == char) and (self.board[8] == char)) or ((self.board[3] == char) and (self.board[6] == char) and (self.board[9] == char)):
            return True
        # checks the diagonals
        elif ((self.board[1] == char) and (self.board[5] == char) and (self.board[9] == char)) or ((self.board[7] == char) and (self.board[5] == char) and (self.board[3] == char)):
            return True
        else:
            return False

    def checkEmptyCell(self, pos):
        if self.board[pos] != '':
            print("This cell is occupied. Try again.")
            return False
        else:
            return True

    def checkFull(self):
        print("\nChecking empty cells . . .\n")
        if '' not in self.board:
            return True
        else:
            return False

    def assignPlayer(self, turn):
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

    def playGame(self, char):

        while True:
            print(f"\n{char}'s turn")
            try:
                pos = int(input("Assign to what cell? "))

                if pos < 1 or pos > 9:
                    print("Cell address out of valid range.")
                    continue

                if self.board[pos] != '':
                    print("This cell is occupied. Try again.")
                    continue

            except ValueError:
                print("Enter a number 1-9 only.")
                continue

            # calls the function to reflect the move
            self.updateboard(self.board, pos, char)

            # show current board status
            self.showboard()

            # check if the current move is a winner
            win_status = self.checkWinner(char)

            # check if the board is all occupied
            isFull = self.checkFull()

            if win_status == True:
                print(f"PLAYER {char} WINS!")
                break
            # check if all cells are empty for draw result
            elif isFull:
                print("Board is full! It's a draw!")
                break
            else:
                # this is the turn of the next player
                char = self.nextMove(char)


# MAIN BODY
while True:
    # show the starting board with its cell address
    TicTacToe.startBoard()

    # create an object of class Tic Tac Toe
    play = TicTacToe()

    # show the empty board
    play.showboard()

    # determine the order of the player
    turn = random.randint(1, 2)

    # Player picks X or O
    char = play.assignPlayer(turn)

    # start the game and display the result
    play.playGame(char)

    again = input("Do you want to play again? Press N for No.")
    if again.upper() == "N":
        print("Goodbye!")
        break
