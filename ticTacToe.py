# ch 5, tic tac toe , not finished. started using the books data structure but am trying the user input on my own

theBoard = {'top-L': 'X', 'top-M': 'O', 'top-R': 'X',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print('   L | M | R   ')
    print('   =========')
    print('1| ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print(' | --+---+--')
    print('2| ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print(' | --+---+--')
    print('3| ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])


print('Welcome, this is Tic Tac Toe.')
printBoard(theBoard)
while True:
    player_move = input('Make your Move. Pick Either X or O: ')
    print('Choose your moves location. Use format "RowColumn". Example: 1')
    player_move_location = input()
