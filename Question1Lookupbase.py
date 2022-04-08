from random import random
import re


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def sign():
    lst = ['X','O']
    return random.choice(lst)


def Condition_Check(board,sign):
    if sign == 'X':
       if board[2] == ' ':
           return 2
    elif sign == 'O':
        if board[3] == ' ':
            return 3
def assignSign(pos,board,sign):
    board[pos] = sign
    

while True:
    theBoard = [' ', ' ', ' ', ' ', ' ', 'X', 'O', ' ', 'X', 'O']
    print(drawBoard(theBoard))
    assignSign(Condition_Check(theBoard,sign()),theBoard,sign())
    print(drawBoard(theBoard))
    if theBoard[8] == 'X' and theBoard[5] == 'X' and theBoard[2] == 'X':
        print("Computer X wins")
    elif theBoard[9] == 'O' and theBoard[6] == 'O' and theBoard[3] == 'O':
        print("Computer O wins")
    x = input("Do wanna play again: ")
    if x == 'n':
        break
    else:
        pass


