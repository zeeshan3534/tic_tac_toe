

import random


def drawBoard(board):
    
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

def inputPlayerLetter():
    
    return ['X', 'O']

def whoGoesFirst():
    # for simplification letteing the computer go first
    # return 'player'
    lst = ['computer1','computer2']
    return random.choice(lst)

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    if computer1Letter == 'X':
        computer2Letter = 'O'
    else:
        computer2Letter = 'X'


    if computer2Letter == board[7] and computer2Letter== board[8]:
        return 9
    elif computer2Letter == board[4] and computer2Letter== board[5]:
        return 6
    elif computer2Letter == board[5] and computer2Letter== board[7]:
        return 3
    elif computer2Letter == board[5] and computer2Letter == board[8]:
        return 2   
    elif computer2Letter== board[4] and computer2Letter == board[7]:
        return 1
    if isSpaceFree(board,3) == ' ' and computer2Letter == board[5] and computer2Letter == board[7]:
        return 3
    elif isSpaceFree(board, 9) == ' ' and computer2Letter == board[1] and computer2Letter == board[5]:
        return 9
    elif isSpaceFree(board, 3) == ' ' and computer2Letter == board[5] and computer2Letter == board[7]:
        return 3
    elif isSpaceFree(board, 1) == ' ' and computer2Letter == board[5] and computer2Letter == board[9]:
        return 1
    elif isSpaceFree(board, 2) == ' ' and computer2Letter == board[5] and computer2Letter == board[8]:
        return 2
    else:
        i=0
        while 1<10:
            if isSpaceFree(board,i ):
                move = chooseRandomMoveFromList(board,[1,2,3,4,5,6,7,8,9])
            i+=1


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computer1Letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer1Letter == 'X':
        computer2Letter = 'O'
    else:
        computer2Letter = 'X'
        

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computer1Letter, i)
            if isWinner(copy, computer1Letter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computer2Letter, i)
            if isWinner(copy, computer2Letter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    # theBoard = [' '] * 10
    theBoard = [' ', 'X', 'O', 'X', 'O', ' ', ' ', ' ', ' ', ' ']
    computer1Letter, computer2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'computer1':

            move = getComputerMove(theBoard, computer1Letter)
            makeMove(theBoard, computer1Letter, move)

            if isWinner(theBoard, computer1Letter):
                drawBoard(theBoard)
                print('The computer 1 has beaten computer 2')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer2'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computer2Letter)
            makeMove(theBoard, computer2Letter, move)

            if isWinner(theBoard, computer2Letter):
                drawBoard(theBoard)
                print('The computer 2 has beaten computer 1')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer1'

    if not playAgain():
        break