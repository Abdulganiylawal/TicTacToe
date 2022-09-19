# Requirements
# 2 players should be able to play the game(both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

# Board

myList = []


class Player:
    name = ""
    turn = ""

    def setName(self):
        name = input("What is the name of the player: ")
        self.name = name

    def setTurn(self):
        while True:
            turn = input("What are you (x or o): ")
            if turn == "x" or turn == "o":
                self.turn = turn
                break
            else:
                print("wrong value")


board = [
    ["0", "|", "1", "|", "2"],
    ["3", "|", "4", "|", "5"],
    ["6", "|", "7", "|", "8"],
]


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="          ")
        print()


def replaceValue(board, value, position):
    patterns = {
        0: (0, 0),
        1: (0, 2),
        2: (0, 4),
        3: (1, 0),
        4: (1, 2),
        5: (1, 4),
        6: (2, 0),
        7: (2, 2),
        8: (2, 4),
    }
    while True:
        if position not in myList:
            x = y = 0
            x, y = patterns[position]
            board[x][y] = value
            myList.append(position)
            break
        else:
            position = int(input(
                "This position has been used. Enter another position: "))
    printBoard(board)


def gameOn():
    print("Welcome to a Tic Tac Toe Game.")
    player1 = Player()
    player1.setName()
    player1.setTurn()
    player2 = Player()
    player2.setName()
    player2.setTurn()
    count = 0
    turn = 0
    playerTurn = input("Who is going first: ")
    printBoard(board)
    while True:
        if playerTurn == "x" or playerTurn == "o":
            if playerTurn == "x":
                position = int(input("What position are you taking: "))
                replaceValue(board, "x", position)
                print("It is o turn")
                playerTurn = "o"
                turn = turn + 1
                count = count + 1
            elif playerTurn == "o":
                position = int(input("What position are you taking: "))
                replaceValue(board, "o", position)
                print("It is x turn")
                playerTurn = "x"
                turn = turn + 1
                count = count + 1
        if (
            board[0][0] == board[0][2] == board[0][4] == "x"
            or board[0][0] == board[1][0] == board[2][0] == "x"
            or board[0][4] == board[1][4] == board[2][4] == "x"
            or board[0][2] == board[1][2] == board[2][2] == "x"
            or board[1][0] == board[1][2] == board[1][4] == "x"
            or board[1][0] == board[1][2] == board[1][4] == "x"
            or board[2][0] == board[2][2] == board[2][4] == "x"
            or board[0][0] == board[1][2] == board[2][4] == "x"
            or board[0][4] == board[1][2] == board[2][0] == "x"
        ):
            if player1.turn == "x":
                print("The winner is {}".format(player1.name))
                break
            elif player2.turn == "x":
                print("The winner is {}".format(player2.name))
                break

        elif (
            board[0][0] == board[0][2] == board[0][4] == "o"
            or board[0][0] == board[1][0] == board[2][0] == "o"
            or board[0][4] == board[1][4] == board[2][4] == "o"
            or board[0][2] == board[1][2] == board[2][2] == "o"
            or board[1][0] == board[1][2] == board[1][4] == "o"
            or board[1][0] == board[1][2] == board[1][4] == "o"
            or board[2][0] == board[2][2] == board[2][4] == "o"
            or board[0][0] == board[1][2] == board[2][4] == "o"
            or board[0][4] == board[1][2] == board[2][0] == "o"
        ):
            if player1.turn == "o":
                print("The winner is {}".format(player1.name))
                break
            elif player2.turn == "o":
                print("The winner is {}".format(player2.name))
                break
            else:
                continue

        elif count == 9:
            print("The game is a draw")


gameOn()
print("The game is over")
