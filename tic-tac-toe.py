#Tic-tac-toe game
#!python3

theBoard = {'top-L':'','top-M':'','top-R':'','mid-L':'','mid-M':'','mid-R':'','low-L':'','low-M':'','low-R':''}
def printBoard(board):
    print('+ + +')
    print(board['mid-L']+ ' | '+board['mid-M'] + '|'+board['mid-R'])
    print('+ + +')
    print(board['low-L']+ ' | '+board['low-M'] + '|'+board['low-R'])

turn = 'x'
for i in range(9):
    printBoard(theBoard)
    print ('Turn for '+ turn + '. Move on which block? ')
    move = input()
    theBoard[move] = turn
    if turn == 'x':
        turn = '0'

    else:
        turn = 'x'
printBoard(theBoard)

