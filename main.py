import os
import random


def clearscreen():
    os.system("cls")


def pause():
    os.system("pause")


def displayboard(board):
    print("+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|   ", board[0][0], "   |   ", board[0][1], "   |   ", board[0][2], "   |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|   ", board[1][0], "   |   ", board[1][1], "   |   ", board[1][2], "   |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|   ", board[2][0], "   |   ", board[2][1], "   |   ", board[2][2], "   |\n",
          "|       |       |       |\n",
          "|-------+-------+-------+", sep="")
    return


def freespace(board, free):
    k = 0
    for i in range(0, 3):
        for j in range(0, 3):
            board[i][j] = free[k]
            k += 1
    return board


def player1move(free):
    move1 = 0

    while move1 == 0:
        move1 = int(input("Please enter the number of a free square: "))
        if move1 < 1 or move1 > 9:
            move1 = 0
        elif move1 >= 1 or move1 <= 9:
            if free[move1 - 1] == 'X' or free[move1 - 1] == 'O':
                move1 = 0
    return move1


def player2move(free):
    move2 = 0

    while move2 == 0:
        move2 = int(input("Please enter the number of a free square: "))
        if move2 < 1 or move2 > 9:
            move2 = 0
        elif move2 >= 1 or move2 <= 9:
            if free[move2 - 1] == 'X' or free[move2 - 1] == 'O':
                move2 = 0
    return move2


def computermove(free):
    move2 = 0

    while move2 == 0:
        move2 = random.randrange(1, 10)
        if move2 < 1 or move2 > 9:
            move2 = 0
        elif move2 >= 1 or move2 <= 9:
            if free[move2 - 1] == 'X' or free[move2 - 1] == 'O':
                move2 = 0
    return move2


def victorycondition(free):
    victory = 0
    if ((free[0] == player1char and free[1] == player1char and free[2] == player1char) or
            (free[3] == player1char and free[4] == player1char and free[5] == player1char) or
            (free[6] == player1char and free[7] == player1char and free[9] == player1char) or
            (free[0] == player1char and free[3] == player1char and free[6] == player1char) or
            (free[1] == player1char and free[4] == player1char and free[7] == player1char) or
            (free[2] == player1char and free[5] == player1char and free[8] == player1char) or
            (free[0] == player1char and free[4] == player1char and free[8] == player1char) or
            (free[2] == player1char and free[4] == player1char and free[6] == player1char)):
        victory = 1
    elif ((free[0] == player2char and free[1] == player2char and free[2] == player2char) or
          (free[3] == player2char and free[4] == player2char and free[5] == player2char) or
          (free[6] == player2char and free[7] == player2char and free[9] == player2char) or
          (free[0] == player2char and free[3] == player2char and free[6] == player2char) or
          (free[1] == player2char and free[4] == player2char and free[7] == player2char) or
          (free[2] == player2char and free[5] == player2char and free[8] == player2char) or
          (free[0] == player2char and free[4] == player2char and free[8] == player2char) or
          (free[2] == player2char and free[4] == player2char and free[6] == player2char)):
        if players == 2:
            victory = 2
        elif players == 1:
            victory = 3
    else:
        l = 0
        for k in range(0, 9):
            if free[k] == "X" or free[k] == "O":
                l += 1
        if l == 9:
            victory = 4
    return victory


clearscreen()

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
players = 0
player1char = ""
player2char = ""
victory = 0
free = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while players == 0:
    players = int(input("How many players? (1-2): "))
    if players != 1 and players != 2:
        players = 0

while player1char == "":
    player1char = input("X or O?:")
    if player1char == "X" or player1char == "x":
        player1char = "X"
        player2char = "O"
    elif player1char == "O" or player2char == "o":
        player1char = "O"
        player2char = "X"
    else:
        player1char = ""

clearscreen()
displayboard(board)

while victory == 0:
    move1 = player1move(free)
    free[move1 - 1] = player1char
    board = freespace(board, free)

    clearscreen()
    displayboard(board)

    if players == 2:
        move2 = player2move(free)
    else:
        move2 = computermove(free)
    free[move2 - 1] = player2char
    board = freespace(board, free)

    clearscreen()
    displayboard(board)

    victory = victorycondition(free)

if victory == 1:
    print("Player 1 wins!")
elif victory == 2:
    print("Player 2 wins!")
elif victory == 3:
    print("Computer wins!")
else:
    print("Draw!")

pause()
