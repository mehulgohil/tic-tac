import random

board = []

def insertLetter(pos, letter):
    board[pos]=letter

def isSpaceFree(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print("------------")
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print("------------")
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    # greater than 1 because we re startng from 1 and 0th element will always be empty
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b, l):
    return ((b[1]==l and b[2]==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l))

def playerMove():
    run=True
    while run:
        move = input("Select positon from 1 to 9:")
        try:
            move = int(move)       #is will call error if user input a character as it cant convert it to integer and will throw a error
            if(move>0 and move<10):
                if isSpaceFree(move):
                    insertLetter(move, 'X')
                    run=False
                else:
                    print("Sorry this space is filled")
            else:
                print("Enter pos between 1 and 9")
        except:
            print("Enter a valid positon")

def botMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0 ] #going through all possible empty space
    move=0

    #making move if bot is winning and also check if player is winning
    for let in ['O', 'X']:
        for i in possibleMoves:
            tempboard = board[:]
            tempboard[i] = let
            if isWinner(tempboard, let):
                return i

    #making move for corener cases
    cornerOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)

    if len(cornerOpen)>0:
        return selectRandom(cornerOpen)

    #making move for center
    if 5 in possibleMoves:
        return 5

    #making moves for edges
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen)>0:
        return selectRandom(edgesOpen)

    return move

def selectRandom(list):
    length = len(list)
    r = random.randrange(0,length)
    return list[r]

def main():
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry you lost")
            break

        if not(isWinner(board, "X")):
            move = botMove()
            if(move==0):    #when player plays and all the spaces are full so bot will return move=0
                print(" ")
            else:
                insertLetter(move, 'O')
                print("Computer plays an O on positon", move,':')
                printBoard(board)
        else:
            print("Congrats you win")
            break


    if(isBoardFull(board)):
        print("Game Tied!!!")

while True:
    x=input("Play Again?(Y/N)")
    if x.lower()=='y':
        for x in range(10):
            board.append(' ')
        print("==========================")
        main()
    else:
        break
