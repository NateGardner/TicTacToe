import os
import random

def clearscreen():
    os.system("cls")

def pause():
    os.system("pause")

def displayboard(board):
    print("+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|   ",board[0][0],"   |   ",board[0][1],"   |   ",board[0][2],"   |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|   ",board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],"   |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|   ",board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],"   |\n",
          "|       |       |       |\n",
          "|-------+-------+-------+",sep="")
    return

def freespace(board):

    return free

def player1move(board,free):
    move1 = 0

    while move1==0:
        move1 = int(input("Please enter the number of a free square: "))
        if move1<1 or move1>9:
            move1 = 0
    return move1

def player2move(board,free):
    move2 = 0

    while move2==0:
        move2 = int(input("Please enter the number of a free square: "))
        if move2<1 or move2>9:
            move2 = 0
    return move2

def computermove(board,free):
    move2 = 0

    while move2==0:
        move2 = random.randrange(1,10)
        if move2<1 or move2>9:
            move2 = 0
    return move2

def victorycondition(board,free):
    victory = 0
    return victory

clearscreen()

board = [[1,2,3],[4,5,6],[7,8,9]]
players = 0
player1char = ""
player2char = ""

victory = 0
free = [1,2,3,4,5,6,7,8,9]

while players==0:
    players = int(input("How many players? (1-2): "))
    if players!=1 and players!=2:
        players = 0

while player1char=="":
    player1char = input("X or O?:")
    if player1char=="X":
        player2char = "O"
    elif player1char=="O":
        player2char = "X"
    else:
        player1char = ""

while victory==0:
    clearscreen()
    displayboard(board)

    move1 = player1move(board,free)

    free = freespace(board)
    clearscreen()
    displayboard(board)
    if players==2:
        move2 = player2move(board,free)
    else:
        move2 = computermove(board,free)

    free = freespace(board)

    victory = victorycondition(board,free)

if victory==1:
    print("Player 1 wins!")
elif victory==2:
    print("Player 2 wins!")
elif victory==3:
    print("Computer wins!")
else:
     print("Draw!")

pause()
